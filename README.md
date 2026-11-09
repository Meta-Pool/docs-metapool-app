# Meta Pool docs

This repository ([Meta-Pool/docs-metapool-app](https://github.com/Meta-Pool/docs-metapool-app)) is the source of the Meta Pool documentation site, built with [Astro Starlight](https://starlight.astro.build/). The live site is [https://docs.metapool.app](https://docs.metapool.app) (`site` in `astro.config.mjs`).

## Publishing / Deploy

**A merge to `main` (or any push to `main`) automatically publishes the live docs site.**

Hosting is DigitalOcean App Platform, configured in [`.do/app.yaml`](.do/app.yaml):

- App name: `docs-metapool-app`
- Static site: `docs`
- `deploy_on_push: true` on branch `main`
- Build command: `npm ci && npm run build`
- `output_dir: dist`

There are no GitHub Actions in this repository. Publishing is handled by DigitalOcean App Platform, not by CI in this repo. After a merge, the site publishes automatically. There is no extra publish step here.

## How to update the docs

For agents and contributors.

Pages are Markdown and MDX under `src/content/docs/`. The sidebar and navigation live in `sidebar.mjs`. The production build also copies pages under `/master` so old URLs keep working (`scripts/copy-master-paths.mjs`, run at the end of `npm run build`).

Workflow:

1. Make changes on a branch.
2. Open a pull request against `main`.
3. Merge only after review.

Merging to `main` is what publishes the site. This repository is the source of truth for the docs site. The old GitBook space is a separate repository and is not the source of truth for this site.

Before editing, search the existing page tree and `sidebar.mjs` so wording stays consistent with what is already published. Do not invent product facts. That includes fee splits and tokenomics percentages. If a split has changed, point to the current MPIP instead of writing new numbers. Today that proposal is [MPIP-32](https://www.metapool.app/mpip?id=32).

Leave these unchanged unless someone explicitly asks:

- Twitter/X `@meta_pool`
- TikTok `@meta_pool_app`
- Medium publication article URLs (`medium.com/meta-pool/…`, `medium.com/nearprotocol/…`)
- `blog.metapool.app` links

The official Medium profile is [https://medium.com/@metapool.app](https://medium.com/@metapool.app).

## Local development

Requires Node.js `>=22.23.4` (`engines` in `package.json`).

```bash
npm ci
npm run dev
```

- `npm run build` — production build into `dist/`. npm runs `prebuild` first, which is `node scripts/check-gitbook-leftovers.mjs`. That script fails the build if GitBook `{%` tags remain under `src/content/docs/`. The build then runs `astro build` and `scripts/copy-master-paths.mjs`.
- `npm run preview` — serve the production build locally.
