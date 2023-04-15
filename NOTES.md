# android-greeting-card-test-python-appium
Notes

* npm init 
```
# the -y option is to skip the questions
npm init -y

# but if I want to create package.json in the local directory
npm init -y --scope=.
```

* Appium UI
Example of Appium UI JSON for Android:
```
{
  "platformName": "Android",
  "platformVersion": "8",
  "deviceName": "Android08",
  "app": "~/Projects/git/android-greeting-card-test-python-appium/apk/GreetingCard.apk",
  "automationName": "UiAutomator2"
}
```

xpath example for "android.widget.TextView":
```
//android.widget.TextView[@text='Hello World!']
```

Identify element by xpath us By.xpath() method:
```
driver.find_element_by_xpath("//android.widget.TextView[@text='Hello World!']")
```

Verify the text of the element:
```
greeting = (By.XPATH, "//android.widget.TextView")
assert self.find(self.greeting).text == "Hello World!"
```
