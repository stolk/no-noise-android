# no-noise-android

##Filters out the noisiest spam from the device log of Android devices.##

If you are annoyed with the deluge of spam coming from 'adb logcat', then this little utility is for you.

The initial reaction to the noisy device log is typically: use the '-s' flag to specify the stuff I want to see.
However, in my opinion this is the wrong way to handle it.
You could be losing valuable log messages from daemons you did not even know existed.

So our motto will be: **Black-list, not white-list!**

So what's the correct way then?
I'm glad you asked:
You need to filter away the tags that you know are completely useless, yet burrying your valuable information with utter spam.
Let's say you are hunting that bug in your groundbreaking new app, do you really want to see that Accuweather is trying to connect to some server, or that the display slightly dimmed due to different light environment? 
Nope, you want to shut those pests right up, for once and for all.

This is where no-noise-android.py comes in.
Just collect all those pesky noisy tags in a single file, one per line.
no-noise-android.py will read the noisy tag database from 'noisy.tags' file, which can be stored in current working directory, or in your ~/.android/ directory.

##Usage##

You need to assemble a collection of noisy tags that you want to get rid of, in the noisy.tags file.
If you decide to use mine, please go over my collection to make sure you will not miss stuff that is important to you, but noisy to me.

Store this file in ~/.android/noisy.tags or in the current working directory.
Then invoke the python script:

```
./no-noise-android.py [deviceid]
```

You can leave out the deviceid if you have only one connected device.

##Dependencies##

 * adb tool from the Android SDK.
 * Python

##Author##

Bram Stolk

email: b.stolk@gmail.com

twitter: @BramStolk

google play: https://play.google.com/store/apps/developer?id=Game+Studio+Abraham+Stolk&hl=en


