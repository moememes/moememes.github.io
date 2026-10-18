# Domain split: original plan

- `moememes/moememes.github.io`: profile at `https://memes.moe`.
- New `moememes/blog` repository: blog at `https://blog.memes.moe`.

## Prepare the blog

Create a public `blog` repository and an empty local checkout outside this
repository, then run:

    python3 scripts/export-blog.py /path/to/blog

Commit and push that checkout. Enable Pages from its branch/root directory.
The export includes all posts and restores the current paginated blog homepage.
Future blog posts should be written in the new repository.

## Switch GitHub Pages domains

The current repository is remotely configured for `blog.memes.moe`.
Release that domain by changing its Pages custom domain to `memes.moe`,
then set the new blog repository's Pages custom domain to `blog.memes.moe`.
Publish the prepared profile changes in the current repository during the
switch. A brief interruption is possible while domains and certificates update.
Enable Enforce HTTPS for both sites once certificates are available.

## Dynadot

Keep `blog` as CNAME → `moememes.github.io`.
Replace the `www` Forward record with CNAME → `moememes.github.io`.
In Domain Records (the apex), replace any forwarding with these four A records:

- `185.199.108.153`
- `185.199.109.153`
- `185.199.110.153`
- `185.199.111.153`

Leave unrelated subdomains, TXT records, and email records unchanged.
Configure GitHub custom domains before changing DNS. With the apex and www
configured, GitHub redirects www to memes.moe.

Verify the profile at the apex and www, and the blog homepage, pagination,
and a post at blog.memes.moe. Existing post files remain in the main repository
so old article paths continue working.

Remote master currently has a newer CNAME commit. Integrate it before pushing;
the desired final CNAME in this repository is `memes.moe`.
