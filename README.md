# Professional Portfolio - Susana Flecha Saura

Professional scientific portfolio created with [Quarto](https://quarto.org/), designed for marine scientists specialized in ocean biogeochemistry.

## 🌊 Description

This portfolio professionally presents the research trajectory, publications, projects, and field experience of Susana Flecha Saura, a marine scientist specialized in ocean biogeochemistry at CSIC.
https://susafle.github.io/portfolio/

## 📁 Project Structure

```
portfolio/
├── _quarto.yml           # Main site configuration
├── index.qmd             # Homepage
├── about/
│   └── index.qmd         # About page
├── publications/
│   └── index.qmd         # Publications list
├── projects/
│   └── index.qmd         # Research projects
├── media/
│   └── index.qmd         # Image gallery
├── blog/
│   └── index.qmd         # Blog (ready for future posts)
├── css/
│   ├── custom.scss       # Custom SCSS styles
│   └── styles.css        # Additional CSS styles
├── img/                  # Images folder
└── docs/                 # Generated site (for GitHub Pages)
```

## 🚀 Installation and Setup

### Prerequisites

1. **Install Quarto**
   - Download from: https://quarto.org/docs/get-started/
   - Follow the instructions for your operating system

2. **Verify installation**
   ```bash
   quarto --version
   ```

### Preview Site Locally

To view the portfolio in your browser:

```bash
quarto preview
```

The site will automatically open at `http://localhost:4200`

### Generate Static Site

To build the complete site:

```bash
quarto render
```

Generated files will be saved in the `docs/` folder

## ✏️ How to Update the Portfolio

### Update Personal Information

Edit `_quarto.yml` to change:
- Site title
- Social media links
- Navigation menu structure

### Add Publications

Edit `publications/index.qmd` and add new publications following the format:

```markdown
**LastName, Initial.**, Coauthors (year).
*Article title*.
**Journal Name**, volume(number), pages.
[DOI: link](URL)
```

### Add Projects

Edit `projects/index.qmd` to include new research projects:

```markdown
### Project Title
**Role**: Your role in the project
**Period**: Dates
**Funding**: Funding agency

Project description...
```

### Add Images

1. Place images in the `img/` folder
2. Reference them in `.qmd` files:

```markdown
![Image description](../img/image-name.jpg)
```

### Create Blog Posts

1. Create a `blog/posts/` folder
2. Create a new folder for each post: `blog/posts/2025-01-15-my-post/`
3. Inside, create an `index.qmd` file:

```markdown
---
title: "Post Title"
description: "Brief description"
author: "Susana Flecha"
date: "2025-01-15"
categories: [research, oceanography]
image: image.jpg
---

Post content...
```

### Modify Styles

- **Colors and theme**: Edit `css/custom.scss`
- **Additional styles**: Edit `css/styles.css`

Current color palette (ocean-inspired):
- Primary: `#006994` (deep ocean blue)
- Secondary: `#4A90A4` (medium ocean blue)
- Success: `#2E8B57` (sea green)

## 🌐 Publishing on GitHub Pages

### Initial Setup

1. **Create repository on GitHub**
   - Go to GitHub and create a new public repository
   - Suggested name: `portfolio`

2. **Initialize Git locally**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Professional portfolio"
   ```

3. **Connect to GitHub**
   ```bash
   git remote add origin https://github.com/your-username/portfolio.git
   git branch -M main
   git push -u origin main
   ```

### Activate GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings**
3. In the sidebar, select **Pages**
4. Under **Source**, select the `main` branch
5. Under **Folder**, select `/docs`
6. Click **Save**

Your site will be available at: `https://your-username.github.io/portfolio`

### Update the Site

Each time you make changes:

```bash
# 1. Generate the updated site
quarto render

# 2. Add changes to Git
git add .

# 3. Create commit
git commit -m "Description of changes"

# 4. Publish
git push
```

GitHub Pages will automatically update your site in a few minutes.

## 📝 Regular Maintenance

### Monthly Tasks

- [ ] Review and update metrics (h-index, citations)
- [ ] Add new publications
- [ ] Update project status

### Annual Tasks

- [ ] Review contact information
- [ ] Update professional experience
- [ ] Refresh research images
- [ ] Check for broken links

## 🛠️ Troubleshooting

### Site doesn't generate correctly

```bash
# Clean previous files
quarto clean

# Regenerate
quarto render
```

### Images don't display

- Verify that paths are correct (use relative paths)
- Make sure images are in the `img/` folder
- Use format: `![text](../img/image.jpg)` from subfolders

### Styles don't apply

- Verify that `_quarto.yml` correctly points to CSS files
- Clean cache: `quarto clean`
- Regenerate: `quarto render`

## 📚 Additional Resources

- [Official Quarto documentation](https://quarto.org/docs/guide/)
- [Quarto Websites guide](https://quarto.org/docs/websites/)
- [Basic Markdown](https://www.markdownguide.org/basic-syntax/)
- [GitHub Pages](https://docs.github.com/en/pages)

## 🔄 Future Updates

Possible improvements to consider:

- [ ] Google Analytics integration
- [ ] Contact form
- [ ] Downloadable resources section (CVs, presentations)
- [ ] Regular blog posts
- [ ] Interactive oceanographic data visualizations
- [ ] Interactive expedition map

## 📧 Contact

For questions about this portfolio:
- **Email**: susana.flecha@csic.es
- **ORCID**: [0000-0003-2826-5820](https://orcid.org/0000-0003-2826-5820)

## 📄 License

© 2025 Susana Flecha Saura. Content created for academic professional use.

---

**Built with** [Quarto](https://quarto.org/) - Open-source scientific and technical publishing system
