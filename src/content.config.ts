import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const faqSchema = z.array(
  z.object({ q: z.string(), a: z.string() }),
).optional();

const services = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/services' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    h1: z.string().optional(),
    slug: z.string(),
    type: z.literal('service').optional(),
    faqs: faqSchema,
    // Optional hero EEAT / trust enhancements (opt-in per service).
    heroEyebrow: z.string().optional(),
    heroBullets: z.array(z.string()).optional(),
    heroShowRating: z.boolean().optional(),
    heroTrustBar: z.boolean().optional(),
  }),
});

const areas = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/areas' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    h1: z.string().optional(),
    slug: z.string(),
    type: z.literal('area').optional(),
    faqs: faqSchema,
  }),
});

export const collections = { services, areas };
