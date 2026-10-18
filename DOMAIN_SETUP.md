# Editing and publishing

All content is edited in `moememes/moememes.github.io`:

- Profile: `_includes/profile.html`
- Blog posts: `_posts/YYYY-MM-DD-title.md`
- Shared appearance: `_layouts/`, `_includes/`, `css/`, and `_sass/`

Push to `master` to publish. GitHub Pages updates the profile at `memes.moe`.
The Publish blog workflow builds a second version with the blog homepage,
then pushes generated files to `moememes/blog`, which serves `blog.memes.moe`.
The profile at `/about/` is also rebuilt from the same source on both domains.

Do not edit the `blog` repository directly: its current files are automatically
replaced on publication. Its Git history preserves the original source.

## Deployment credential

The source repository's Actions secret `BLOG_DEPLOY_KEY` holds an SSH private
key. Its public key is registered as a write-enabled deploy key only on
`moememes/blog`. It is not a personal access token.

## Troubleshooting

Check Actions → Publish blog in the source repository. The workflow builds
before updating the published files; a failed build leaves the blog unchanged.
It can also be run manually with Run workflow.

Both Pages sites deploy from their branch root: `master` for the source and
`main` for the generated blog. Keep their custom domains set to `memes.moe`
and `blog.memes.moe`, respectively, with HTTPS enabled. No DNS changes are
needed for normal publishing.
