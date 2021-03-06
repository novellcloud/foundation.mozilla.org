/**
 * This is not technically a "config", but the actual run script that
 * invokes ESBuild (https://esbuild.github.io) on the various libraries
 * that we need bundled and written to our frontend's js directory.
 *
 * As a normal script, this should be invoked using node, and it can
 * take a runtime argument `--node-env` followed by either the string
 * "production" or "development" so that process.env.NODE_ENV in our
 * code gets interpreted correctly.
 */
const { build } = require(`esbuild`);
const path = require(`path`);

const arg = process.argv.indexOf(`--node-env`);
const mode =
  arg > 0 ? process.argv[arg + 1] : process.env.NODE_ENV || `development`;
const inProduction = mode === `production`;

const inDir = `./source/js/`;
const outDir = `./network-api/networkapi/frontend/_js/`;

const sources = [
  `main.js`,
  `foundation/pages/mozfest/index.js`,
  `foundation/pages/directory-listing-filters.js`,
  `buyers-guide/bg-main.js`,
  `polyfills.js`,
];

const base = {
  bundle: true,
  watch: !inProduction,
  sourcemap: !inProduction,
  minify: inProduction,
  loader: {
    ".js": "jsx",
    ".jsx": "jsx",
  },
  define: {
    "process.env.NODE_ENV": JSON.stringify(mode),
  },
  inject: [`esbuild.react.shim.js`],
};

sources.map((source) => {
  const opts = Object.assign({}, base);
  opts.entryPoints = [`${inDir}${source}`];
  opts.outfile = `${outDir}${path
    .basename(source)
    .replace(`.js`, `.compiled.js`)}`;
  return build(opts);
});
