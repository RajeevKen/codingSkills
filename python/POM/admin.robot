***setting***
Library     SeleniumLibrary

***variables***

${nextButton}         //cls[@name = "nextButton"]

${Dropdown}         //cls[@title = "drpDn"]

***keywords***


click on Next Button
...
Author : __name
Click on next Button

...

    ${status}    Element is visible     ${nextButton} 

    if  ${status} is True, click Element  ${nextButton}


Get window gandle

    ${femeId}   get Window Handle 

select new Window

    ${windowId}     Get window gandle
    
    Switch to Window    ${windowId}

select elements from Dropdown

[Arguemnts]     ${elementToselect}


Select Element from Drop Dropdown   ${Dropdown}     ${elementToselect} 