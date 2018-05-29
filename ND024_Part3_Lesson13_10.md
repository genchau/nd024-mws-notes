# Lesson 13.10 Continuous Integration

Continuous integration is the idea that we're always making sure our code can be integrated with the remote repository. So across a team, we'll always have a stable build. Now we don't go into details on CI, as much of it is already covered in the dev ops udacity course. But a key lesson here is that Ci in the cloud provides a great place for our time intensive tasks. In particular, our unit tests. A cloud solution like Jenkins will watch the commits going into our repository and trigger any terminal command we feed it. So if you take the Gulp test task that we've just created and hook it up in the cloud, it means that the test suite will run after every commit. But on a completely different computer, letting us go in coding. If one of these tests now fails, we've got an email and can fix it in our next commit. We'll leave our task as is for now, but do go and check out the dev ops Udacity course when we're finished with ours.

[Continuous Integration](https://classroom.udacity.com/courses/ud611/lessons/4225318865/concepts/44585989490923) in Udacity Intro to DevOps course

- - -
Next up: [Lesson Outro](ND024_Part3_Lesson13_11.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
