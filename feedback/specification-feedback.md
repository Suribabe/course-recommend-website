Project Specification Feedback
==================

Commit graded: 7134f89d455567ddfe477d66ede733f24fcb0cb2

Note: The grades for each section represent the completeness of your specification, and do not necessarily reflect how we judge the scope of your project. We still have concerns about the project being different enough from Grumblr - see the additional information section.

### The product backlog (10/10)

* You should have included a clear assignment of responsibility for each feature, to the student or students on the team who will complete that feature. Each student should have sole responsibility for some features on the overall project.
* You should have included a cost estimate for each feature, in hours.  If the cost estimate is more than 5 or 8 hours, you should consider breaking the feature into smaller work units to improve your ability to track progress on it.

### Data models (9/10)

* `location` as a `CharField` may not be the be representation - think carefully about how you want to represent a location (lat/long, address, etc.)
* I'm confused by your `Recommendation` model - lists cannot be represented by a foreign key relationship.

### Wireframes or mock-ups (10/10)

### Additional Information

* You mention using the Google Maps API to reverse image search - as far as I can tell, this API does not exist.
* You mention using the Instagram API to authenticate users - the Instagram API is only available in a "sandbox mode" until you are approved by Instagram. This means that you won't be able to use real Instagram data.
* I like the idea of a post/user recommendation system, and I would encourage you to dive deeper into that in order to make this an interesting application that differs significantly from grumblr. This currently still feels like grumblr plus some extensions - those extensions will need to be fairly complex in order to make this a non-trivial project.

---
#### Total score (29/30)
---
Graded by: Jacob Brooks (jacobbro@andrew.cmu.edu)

To view this file with formatting, visit the following page: https://github.com/CMU-Web-Application-Development/Team197/blob/master/feedback/specification-feedback.md
