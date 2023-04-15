# android-greeting-card-test-python-appium

This is a sample Python Appium test for Android Greeting Card app.

## Prerequisites
* macOS
* Homebrew
* Android Studio
* Android SDK
* Android Emulator
* Python 3.11.2
* pipenv

## Setup
1. Install [pyenv](https://github.com/pyenv/pyenv)
```
brew update
brew install pyenv
```

2. Install python
```
pyenv install 3.11.2
pyenv global 3.11.2
```

3. [Install](https://pipenv.pypa.io/en/latest/installation/#installing-pipenv) [pipenv](https://github.com/pypa/pipenv)
```
install pipenv --user
```

Per the docs:
Note:
This does a `user installation`_ to prevent breaking any system-wide
packages. If `pipenv` isn't available in your shell after installation,
you'll need to add the user site-packages binary directory to your `PATH`.

On Linux and macOS you can find the user base binary directory by running
`python -m site --user-base` and adding `bin` to the end. For example,
this will typically print `~/.local` (with `~` expanded to the
absolute path to your home directory) so you'll need to add
`~/.local/bin` to your `PATH`. You can set your `PATH` permanently by
`modifying ~/.profile`_.

---

Updated .zshrc:
```
# pipenv
export PATH=~/.local/bin:$PATH
```

4. Install python dependencies:
```
pipenv install
```

5. Install [Appium](https://appium.io/docs/en/about-appium/getting-started/?lang=en) in the project directory:
```
npm i
```

6. Install the UiAutomator2 Driver:
```
npx appium driver install uiautomator2
```


## Run
1. Start Appium server:
```
npx appium
```

2. Run tests:
```
pipenv run pytest -m "id:greeting"
```

