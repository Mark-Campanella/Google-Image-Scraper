# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
import os
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable


def worker_thread(search_key):
    image_scraper = GoogleImageScraper(
        webdriver_path, 
        image_path, 
        search_key, 
        number_of_images, 
        headless, 
        min_resolution, 
        max_resolution, 
        max_missed)
    image_urls = image_scraper.find_image_urls()
    with open(os.path.join(image_path, f"{search_key}_urls.txt"), "w", encoding="utf-8") as f:
        for url in image_urls:
            f.write(url + "\n")
    image_scraper.save_images(image_urls, keep_filenames)

    #Release resources
    del image_scraper

if __name__ == "__main__":
    #Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys = list(set([
    "cv5013ec4",
    "wqb245axuc",
    "wt8400c",
    "wt8480c",
    "gte17dtn",
    "grsn2620a",
    "wtw87nh1uc",
    "elfw7738",
    "elte7300",
    "fdsp4401",
    "ldph555",
    "fv3011wb4",
    "rb50",
    "bwk17abana",
    "ma512w160/wk-04",
    "if55",
    "wa55cg71a",
    "wa55a73a",
    "ptw800bw",
    "dv45dg60h",
    "dv25b69h",
    "wm9901ha",
    "wm9900ha",
    "wf51cg80a",
    "wkhc152ha",
    "sgx78c55uc",
    "pdsh4816",
    "fght2055v",
    "gne27jgm",
    "wdps7024rz",
    "lrdcs2603",
    "cra30fbana",
    "wd11m4473pw/az",
    "lsp11",
    "cwb09bbana",
    "bnc10asana",
    "na-f140b6wb / na-f140b6tb",
    "led13",
    "ib45s",
    "crm44abana",
    "ptw700bt",
    "rt42",
    "rf691f",
    "mhw3500fw0",
    "wf53bb87a",
    "wfw5605mw",
    "wtw7500gw0",
    "wtw8700ec0",
    "mvwb955fw0",
    "mvw5435pw",
    "mfw7020rf",
    "wtw4816fw",
    "mvw5430mw",
    "mvwc565fw1",
    "wtw4957pw",
    "wfw5090gw0",
    "wfw9290fw0",
    "mhw5630hw",
    "dlhc1455",
    "md-rt4",
    "wgd4950hw",
    "mrt311fffh",
    "bno10abana",
    "dwhd661efp",
    "kdte304rps",
    "wdt550sapz",
    "ls27t3230",
    "mfc2062fez",
    "wrm54bktww",
    "ww11j4473pw/az",
    "wrt312czjb",
    "ldts555",
    "wfw560chw",
    "mys20pdw",
    "mdfs3924rz",
    "med7230hw",
    "wed5605mw",
    "med4500mw",
    "na-f120b1wb / na-f120b1tb",
    "cwh12bbana",
    "mf200w125wb/gk-01",
    "lac11",
    "bwk13abana",
    "ma500w13/wg-01",
    "brm44hbana",
    "bre57fkana",
    "mf200d130wb/gk-01",
    "lfe11",
    "blf14arbna"
]))

    #Parameters
    number_of_images = 2                # Desired number of images
    headless = False                    # True = No Chrome GUI
    min_resolution = (0, 0)             # Minimum desired image resolution
    max_resolution = (9999, 9999)       # Maximum desired image resolution
    max_missed = 10                     # Max number of failed images before exit
    number_of_workers = 3               # Number of "workers" used
    keep_filenames = True              # Keep original URL image filenames

    #Run each search_key in a separate thread
    #Automatically waits for all threads to finish
    #Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)
