# AOPS-AMC-Datascraper
Revised from https://github.com/ryanrudes/amc because of the recent Selenium changes.

>I do not claim the rights to this content; the MAA's contest problems are publicly released on the AoPS website, found [here](https://artofproblemsolving.com/wiki/index.php/AMC_Problems_and_Solutions).
>
>Note: If you have created a directory named AMC in your home folder in the past, the code will erase its content, overwriting it with datascraped AMC problems.
>
>This repository contains problems from AMC 10, but a slight modification of the code can scrape problems from AMC 12, or 8 as well. Note that the URL for AMC 8 problems does not contain an "A" or a "B" because AMC 8 contests do not have multiple exam dates. You will have to modify the URL accordingly.
>
>There may be a few problems that appear to be missing from the data; this is due to the fact that the AMC repeats contest problems every so often, so some URL's are redirected to, say the AMC 12 when requesting an AMC 10 problem. These missing problems can be found under some AMC 12 competition.
>
>Possible changes in the AoPS website in the future may render this code dysfunctional.
>
-**[ryanrudes](https://github.com/ryanrudes/amc/blob/main/README.md)**

Recent Selenium changes allows usage of this code without a chromedriver executable.

This code, when ran in Visual Studio Code, tends to save the "AMC" folder in the VS Code folder opened rather than the "home directory" typically considered as C:\Users\username.

## Required Installs
```py
pip install Selenium

pip install numpy

pip install pillow
```

