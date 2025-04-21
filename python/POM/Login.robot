***setting***
Library     SeleniumLibrary

***variables***

${url} = www.google.com

${userName} = dummy_ser

${password} = password

${dropDownElement} = 

${visibilityXpath}      //img[@title = "google"]

${userNamePath}         //cls[@name = "username"]
${passwordPath}         //cls[@name = "password"]

***keywords***


Navigate to Url

    [Arguments]     ${url}

    open Browser    ${url}

    Wait for element to be visible      ${visibilityXpath}


Login to site

    [Arguments]     ${userName}     ${password}

    Element is visible      ${userNamePath}
    Input Test      ${userNamePath}     ${userName}
    Element is visible      ${passwordPath}
    Input Test      ${passwordPath}     ${password}

    Sleep 3s
    // sync code

