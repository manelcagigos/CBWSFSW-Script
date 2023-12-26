# CBWSFSW-Script 📄
CBWSFSW stands for: `Close Browsers When Searching For Specific Words`.

When using this script if you search for the words that you declare inside the code in Firefox or Chrome browsers, it would automatically close your explorer (It only works with Firefox and Chrome, but it should be easy to make it work on other browsers, like Edge, Brave or Opera for example).

I also made that the script works when the word you are searching is inside an URL, for example, if you are on Instagram and search for Potato and you click on the profile of someone that has potato in his name it will appear in the URL (www.instagram.com/potato) and the script will detect that and close the browser.

It's a pretty invasive way of doing this, the script goes inside your local files and search for the database files of the browsers and execute the commands to search for the words in specific, so I would recommend using it in your own profile and devices, it's safe to use but it could slow down your computer.

> [!TIP]
> I would recommend doing a .bat file so that you can program this script to start automatically when you log in with your user in your computer, the script is made to work all the time, so it won't stop if you don't stop it manually.

> [!CAUTION]
> **Use it at your own responsibility, I'm not responsible, and I'm not in charge of any wrong use of the script**.

> [!NOTE]
> In the script you need to change `<User>` for your computer user profile name, and you also need to change `<Firefox-default-profile>` for your own profile, it should be localted in the same route before where you should put the correct name, and if you need it, you can change the disk where the path is located, `C:`.

#

### Bibliography

Here you can find all the links to the webpages that I used to make this script

- https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data
- http://kb.mozillazine.org/Profile_Manager
- https://support.mozilla.org/en-US/questions/772293
- https://wiki.mozilla.org/Firefox/CommandLineOptions
- https://askubuntu.com/questions/412844/can-i-view-firefox-history-with-the-terminal
- https://docs.nxlog.co/integrate/browser-history.html
- https://chat.openai.com/
