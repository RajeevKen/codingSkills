***settings***
Librry  SeleniumLibrary

Objects     POM\admin.robot
Objects     POM\login.robot
Objects     Data\inputData.robot



***variables***



***keywords***

***Test Cases***

Navigate to site and Select elements from drop Dropdown
...
    [Arguments]
    [Tags]      Regression  Smoke

    Navigate to Url     ${url}

    Login to site       ${creds}[username]    ${creds}[password]

    click on Next Button

    select new Window



""""
Robot Framework Scenario using Python
 
Launch Browser 
Enter URL
Enter User Name and Password
Click on Next Button
New Window get Open
Navigate to  Window
Select a value from Dropdown
"""