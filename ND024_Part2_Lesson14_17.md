# Lesson 14.17 Atomic Relevant Busy

There are 3 attributes which work with aria-live to fine tune what is communicated to the user when the live region changes. 

`aria-atomic` indicates whether the entire region should be considered as a whole when communicating updates. 
`aria-relevant`indicates what types of changes should be presented to the user. Options are `additions` `removals` or `text`.
`aria-busy` lets us notify a specific technology that it should temporarily ignore changes to this element, such as when things alerting say after a temporary connectivity lapse. Once everything is back in place, aria-busy should be set to false.

- - -
Next up: [Recap](ND024_Part2_Lesson14_18.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
