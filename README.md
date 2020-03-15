# covid19-status

## Visualization
* https://justinlewis.github.io/covid19-status-colorado/

### About
The Colorado Department of Public Health publication for providing status updates for COVID-19 is overloaded and not the best visualization. Let's make it better.


### Hopes & Dreams
Create a basic visualization
* Could start by pushing to the Carto API.

### Data Sources
* https://docs.google.com/document/d/e/2PACX-1vRSxDeeJEaDxir0cCd9Sfji8ZPKzNaCPZnvRCbG63Oa1ztz4B4r7xG_wsoC9ucd_ei3--Pz7UD50yQD/pub

### Potential Supplemental Data Sources
* https://github.com/CSSEGISandData/COVID-19

### How To Dev
Thank you!

#### Setup local
Setup a simple local Node server to help with localhost cross domain issues.
1. Setup local NPM HTTP server with 'sudo npm i http-server -g'
2. CD into root project directory and run 'http-server'

#### Updating data
To keep this simple we're hosting on Github Pages and therefore don't have a database or ability to run automatic data updates. However, updates can be done manually on a local dev environment easily.
1. Pull the latest code.
2. Run the get_it.py (no params needed) file which will update colorado.js with the latest data.
3. Push the updated data to the repository.
4. Bam! You just helped your community stay up to date!
