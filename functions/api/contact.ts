// Cloudflare Pages Function: handles contact form submissions.
// Accepts application/x-www-form-urlencoded or multipart/form-data
// from the contact page form and forwards to a configured destination.
//
// Env vars (set in CF Pages dashboard):
//   CONTACT_EMAIL_TO       - primary recipient (e.g. info@customfabriccreations.net)
//   CONTACT_WEBHOOK_URL    - optional alternate webhook destination (Slack, Make, Zapier)
//
// Graceful fallback: if no delivery method is configured, the submission is
// logged to CF Pages analytics but the user is still redirected to /thank-you/
// so the funnel doesn't break during setup.

interface Env {
  CONTACT_EMAIL_TO?: string;
  CONTACT_WEBHOOK_URL?: string;
  RESEND_API_KEY?: string;
}

// GoHighLevel webhook-trigger fallback. The CONTACT_WEBHOOK_URL env var
// takes precedence if set, so the URL can be rotated in the CF Pages
// dashboard without a code change.
const DEFAULT_WEBHOOK_URL =
  'https://services.leadconnectorhq.com/hooks/Xg4LNpuuKN5aNBM9djkU/webhook-trigger/3290635e-00f9-43ed-9547-850c1368d5a6';

export const onRequestPost: PagesFunction<Env> = async ({ request, env }) => {
  let payload: Record<string, string> = {};
  try {
    const contentType = request.headers.get('content-type') ?? '';
    if (contentType.includes('application/json')) {
      payload = (await request.json()) as Record<string, string>;
    } else {
      const form = await request.formData();
      for (const [k, v] of form.entries()) {
        payload[k] = typeof v === 'string' ? v : '';
      }
    }
  } catch (err) {
    return new Response('Bad request', { status: 400 });
  }

  // Honeypot + basic validation
  const required = ['name', 'email', 'phone'];
  for (const field of required) {
    if (!payload[field] || payload[field].trim().length < 2) {
      return new Response(`Missing field: ${field}`, { status: 400 });
    }
  }

  const fullName = (payload.name ?? '').trim();
  const nameParts = fullName.split(/\s+/);
  const firstName = nameParts[0] ?? '';
  const lastName = nameParts.slice(1).join(' ');

  const submission = {
    timestamp: new Date().toISOString(),
    name: fullName,
    full_name: fullName,
    first_name: firstName,
    last_name: lastName,
    email: payload.email,
    phone: payload.phone,
    street: payload.street ?? '',
    address: payload.street ?? '',
    address1: payload.street ?? '',
    area: payload.area ?? '',
    city: payload.area ?? '',
    service: payload.service ?? '',
    space: payload.space ?? '',
    message: payload.message ?? '',
    notes: payload.message ?? '',
    source: 'customfabriccreations.net contact form',
    ip: request.headers.get('cf-connecting-ip') ?? '',
    ua: request.headers.get('user-agent') ?? '',
  };

  const deliveryTasks: Promise<Response | void>[] = [];

  // Webhook (GHL by default, override via CONTACT_WEBHOOK_URL env var)
  const webhookUrl = env.CONTACT_WEBHOOK_URL || DEFAULT_WEBHOOK_URL;
  if (webhookUrl) {
    deliveryTasks.push(
      fetch(webhookUrl, {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify(submission),
      }).catch(() => undefined),
    );
  }

  // Optional Resend email
  if (env.RESEND_API_KEY && env.CONTACT_EMAIL_TO) {
    const body = {
      from: 'Custom Fabric Creations <website@customfabriccreations.net>',
      to: env.CONTACT_EMAIL_TO,
      reply_to: submission.email,
      subject: `New consultation request \u2014 ${submission.name}`,
      text: [
        `Name: ${submission.name}`,
        `Email: ${submission.email}`,
        `Phone: ${submission.phone}`,
        `Address: ${submission.street}`,
        `City: ${submission.area}`,
        `Service: ${submission.service}`,
        '',
        'Message:',
        submission.message,
        '',
        '\u2014',
        `Submitted: ${submission.timestamp}`,
      ].join('\n'),
    };
    deliveryTasks.push(
      fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'content-type': 'application/json',
          authorization: `Bearer ${env.RESEND_API_KEY}`,
        },
        body: JSON.stringify(body),
      }).catch(() => undefined),
    );
  }

  await Promise.allSettled(deliveryTasks);

  // Log to CF analytics regardless (shows up in Pages analytics)
  console.log('Contact submission', JSON.stringify(submission));

  // Redirect to thank-you
  return Response.redirect(new URL('/thank-you/', request.url).toString(), 303);
};

// Block other methods
export const onRequest: PagesFunction = async ({ request }) => {
  return new Response('Method not allowed', { status: 405 });
};
