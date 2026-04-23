import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const faqSchema = z.array(
  z.object({ q: z.string(), a: z.string() }),
).optional();

const services = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/services' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    h1: z.string().optional(),
    slug: z.string(),
    type: z.literal('service').optional(),
    faqs: faqSchema,
  }),
});

const areas = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/areas' }),
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
