import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightLlmsTxt from 'starlight-llms-txt';
import sidebar from './sidebar.mjs';

export default defineConfig({
	site: 'https://docs.metapool.app',
	integrations: [
		starlight({
			title: 'Meta Pool Docs',
			description:
				'Meta Pool objective is to provide easy and permissionless access to Web3 financial tools for everybody',
			favicon: '/favicon.png',
			head: [
				{
					tag: 'link',
					attrs: {
						rel: 'icon',
						href: '/favicon.png',
						type: 'image/png',
						sizes: '512x512',
					},
				},
				{
					tag: 'link',
					attrs: {
						rel: 'apple-touch-icon',
						href: '/apple-touch-icon.png',
						sizes: '512x512',
					},
				},
			],
			sidebar,
			plugins: [starlightLlmsTxt({ projectName: 'Meta Pool' })],
			components: {
				ThemeProvider: './src/components/ThemeProvider.astro',
			},
		}),
	],
});
