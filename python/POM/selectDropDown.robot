***settings***
Library     SeleniumLibrary


***variables***
${url}      www.google.com
${dropwordXpath}        //dp[@name='dropDown']
${dropDownVlue}
${loaderXpath}      //d[@title='loader']


***keywords***
Launch Browser
[Arguments]     ${url}
    Open Browser    chrome  ${url}
    // add sync or sleep
    sleep 5s

select Drop Down Element
[Arguments]     ${itemToSelect}
    
    ${flag}     Element is visible  ${dropwordXpath}, Falied due element is not visible
    if  ${flag} is True    Run keyword      Select Elment From Dropdown     ${dropwordXpath}    ${dropDownVlue}


Sync Page
[Arguments]     ${loaderXpath}
    ${flag}     True
    WHILE   ${flag} is True
        ${flag}     Run keyword And Return status   Element Is Visible      ${loaderXpath}
        Sleep   3s
    
***Test Cases***

Test Select Element from drop down
...
Doc String
_Auther :
...

[Arguments]     ${url}      ${elementToSelect}

[Tags]      Smoke

    Launch Browser      ${url}

    select Drop Down Element        ${elementToSelect}