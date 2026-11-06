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
			sidebar,
			plugins: [starlightLlmsTxt({ projectName: 'Meta Pool' })],
			components: {
				ThemeProvider: './src/components/ThemeProvider.astro',
			},
		}),
	],
});
