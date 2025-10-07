# Waxly Deployment Guide

This guide walks you through the manual steps needed to complete the Waxly deployment to GitHub Pages with the custom domain hellowaxly.com.

## ✅ Already Completed (via code)

The following has been automatically configured in the codebase:

- ✅ All files rebranded to "Waxly"
- ✅ CNAME file created with `hellowaxly.com`
- ✅ GitHub Actions workflow created for automatic deployment
- ✅ MkDocs configuration updated
- ✅ Custom CSS styling added
- ✅ Documentation updated

## 📋 Manual Steps Required

### Step 1: Rename the GitHub Repository

1. Go to your repository on GitHub: `https://github.com/darthrootbeer/vinyl-lexicon`
2. Click **Settings** (top navigation)
3. Scroll down to **Repository name**
4. Change the name from `vinyl-lexicon` to `waxly`
5. Click **Rename**

**Note:** After renaming, your repository URL will be `https://github.com/darthrootbeer/waxly` (or if you create a new org, `https://github.com/waxly/waxly`)

### Step 2: Set Repository to Public

1. In **Settings**, scroll down to **Danger Zone**
2. Click **Change visibility**
3. Select **Make public**
4. Confirm by typing the repository name
5. Click the confirmation button

**Why?** GitHub Pages requires public repositories (unless you have GitHub Pro/Team/Enterprise)

### Step 3: Enable GitHub Pages

1. In **Settings**, click **Pages** in the left sidebar
2. Under **Source**, select:
   - **Deploy from a branch** ➜ Change to **GitHub Actions**
3. This will allow the automated workflow to deploy your site

### Step 4: Configure DNS at Your Domain Registrar

Go to your domain registrar (where you purchased hellowaxly.com) and add these DNS records:

#### A Records (for apex domain)
Add **four** A records, all pointing to GitHub's IPs:

```
Type: A
Name: @ (or leave blank for root domain)
Value: 185.199.108.153

Type: A
Name: @ (or leave blank)
Value: 185.199.109.153

Type: A
Name: @ (or leave blank)
Value: 185.199.110.153

Type: A
Name: @ (or leave blank)
Value: 185.199.111.153
```

#### CNAME Record (for www subdomain)
```
Type: CNAME
Name: www
Value: darthrootbeer.github.io (or waxly.github.io if using org)
```

**Note:** DNS changes can take 24-48 hours to propagate globally, but often work within an hour.

### Step 5: Verify Custom Domain in GitHub

1. Go back to **Settings** → **Pages**
2. Under **Custom domain**, you should see `hellowaxly.com` (from the CNAME file)
3. Wait for DNS check to complete (green checkmark)
4. Once verified, check **Enforce HTTPS** (highly recommended)

### Step 6: Push Changes and Deploy

1. Commit all the changes to your repository:
   ```bash
   git add .
   git commit -m "Rebrand to Waxly and setup GitHub Pages"
   git push origin main
   ```

2. The GitHub Actions workflow will automatically:
   - Build the MkDocs site
   - Deploy to GitHub Pages
   - Make it available at hellowaxly.com

3. Check the **Actions** tab in GitHub to monitor the deployment

### Step 7: Verify the Live Site

Once deployment completes (usually 2-5 minutes):

1. Visit `https://hellowaxly.com`
2. Verify the site loads correctly
3. Test navigation and search functionality
4. Check that the custom styling appears correctly

## 🎨 Optional: Create a Favicon

To add a custom favicon (the small icon that appears in browser tabs):

1. Create or generate a 32x32 pixel PNG image with:
   - Matte black background (#0a0a0a)
   - Circular record design
   - Warm gold center (#ffb400)

2. Convert to `.ico` format using an online tool like:
   - https://favicon.io/favicon-converter/
   - https://convertio.co/png-ico/

3. Save as `favicon.ico` in the `docs/` folder

4. Add to mkdocs.yml under the `theme` section:
   ```yaml
   theme:
     favicon: favicon.ico
   ```

5. Commit and push

## 🔧 Troubleshooting

### Custom Domain Not Working

- **DNS not propagated**: Wait 24-48 hours, or use `dig hellowaxly.com` to check
- **CNAME file missing**: Verify `docs/CNAME` contains exactly `hellowaxly.com`
- **HTTPS errors**: Wait for GitHub to provision SSL certificate (can take a few minutes)

### Build Failing

- Check the **Actions** tab for error messages
- Verify all Python dependencies are in `requirements.txt`
- Test locally with `mkdocs build` to catch errors

### Styling Not Appearing

- Clear browser cache (Cmd+Shift+R or Ctrl+Shift+F5)
- Verify `docs/assets/stylesheets/waxly.css` exists
- Check that `mkdocs.yml` includes the CSS in `extra_css`

## 📞 Need Help?

If you encounter issues:

1. Check the GitHub Actions logs in the **Actions** tab
2. Review GitHub's documentation: https://docs.github.com/en/pages
3. Verify DNS settings with your domain registrar
4. Test the site locally first: `mkdocs serve`

## 🎉 Success Checklist

- [ ] Repository renamed to `waxly`
- [ ] Repository set to public
- [ ] GitHub Pages enabled (using GitHub Actions)
- [ ] DNS records configured
- [ ] Custom domain verified in GitHub Settings
- [ ] HTTPS enforced
- [ ] Changes pushed to main branch
- [ ] Deployment completed successfully
- [ ] Site accessible at https://hellowaxly.com
- [ ] Styling and branding correct
- [ ] Navigation and search working

---

**Once complete, Waxly will be live at https://hellowaxly.com!** 🎶
