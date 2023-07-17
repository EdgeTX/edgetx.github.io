***Please note:*** **This repository is for the EdgeTX Web page.**  

If you would like to report an issue with the EdgeTX webpage, please create an issue with the link below.
 [EdgeTX Website Issues](https://github.com/EdgeTX/edgetx.github.io/issues/new/choose)
 
 
If you would like to report an issue with the EdgeTX software, please create an issue with the link below.
[EdgeTX Software Issues](https://github.com/EdgeTX/edgetx/issues/new/choose)

# How to contribute to the EdgeTX.org website

For small changes (spelling errors or re-phrasing cetain blocks of text) you can simply open the affected .md file and edit it in the browser. Once complete, submit is as a pull request

For bigger changes (new pages, core website changes)

1. Create a fork of the edgetx.github.io repository to your private Github account.
2. Deploy your fork via github pages (this will allow us later to preview your proposed changes online). https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

   ***---Recommended---***
4. Install MKDocs material on your local computer. https://squidfunk.github.io/mkdocs-material/getting-started
5. Clone your forked repository locally to your computer.

   ***The two steps above will allow you to make changes to the website and see the changes immediately on your local machine.***

6. Make the proposed changes and push the changes to your forked repo online.
7. Create a pull request (PR) for the Master repository, describing the changes and including a link to your deployed forked page.
8. Once the PR is accepted, it will be merged to the Master branch and deployed.

## File Directory Structure
/edgetx.github.io/mkdocs.yml  = MK docs configuration file (https://squidfunk.github.io/mkdocs-material/setup/)

/edgetx.github.io/docs/ = Contains individual page .md files

/edgetx.github.io/docs/assets = Contains images for the webpages

/edgetx.github.io/docs/stylesheets = this is where you can customize the CSS for the webpage (https://squidfunk.github.io/mkdocs-material/customization/)

/edgetx.github.io/downloads = storage folder for files to link for downloading

/edgetx.github.io/overrides/ =  this is where individual HTML overide files are placed (current main.html file has annoucement banner text.
