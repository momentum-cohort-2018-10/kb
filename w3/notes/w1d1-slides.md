# Intro to **HTML**

## The structure of web pages

---

# A short history of the web

[Tim Berners-Lee](https://en.wikipedia.org/wiki/Tim_Berners-Lee), English engineer and computer scientist
- while working at CERN, a nuclear research facility in Switzerland, he developed his ideas for what would eventually become the World Wide Web
- His demo page, [THE FIRST WEBPAGE](http://www.ibiblio.org/pjones/old.page.html)

---

# W3C

- Tim Berners-Lee is now the director of the World Wide Web Consortium, or the [W3C](https://www.w3.org/), which was established in 1994 and oversees standards for the web
- When we talk about standards and spec, we're referring to the W3C
  - standards lay out in detail what is valid HTML, CSS, and some JS APIs, although standards for the JS language are governed by ECMA international

---

# Browsers

- the first web browser (or client) was NCSA Mosaic (National Center for Supercomputing Applications) released in Jan 1993
  - these people went on to form a company that created Netscape Navigator which was released in Dec. 1994
  - Internet Explorer released 1995
  - Netscape Navigator project evolved into Firefox
  - Firefox 2002
  - Safari 2003
  - Chrome released September 2008

---

# Some historical examples

- [CNN 1996 Year in Review](http://www.cnn.com/EVENTS/1996/year.in.review/)
- spec for CSS 1 released in that year
- [archived presidential websites](https://www.archives.gov/presidential-libraries/archived-websites)
- [original Amazon website 1994](https://i.dailymail.co.uk/i/pix/2012/01/18/article-2088445-0F82815A00000578-513_634x413.jpg)

---

# HTML: what is it?

- HyperText Markup Language
- describes the structure of the page's content; like the skeleton of the page
- with CSS and JS -- styling, behavior
- markup: a system for annotating a document in a way that is syntactically distinguishable from the text.(wikipedia)
  - "marking up" the content of a document
  - paragraphs get "p" tags, divisions of a page get "div" tags, buttons get a "button" tag, etc.
- page source for momentumlearn.com

---

# Tags vs Elements

- A tag is one part of an element. An opening and a closing tag form a pair
- Or a void or empty element, or a self-closing tag
  - these have no content, although they do often have attributes
  - img, br, hr, input, meta, link
- [MDN HTML Element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

---

# Anatomy of an element

- opening and closing tag, content (text/optional), attributes
- attributes are contained in the opening/start tag
  - Element-specific attributes [standard attributes MDN ref](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)
  - global attributes -- can be applied to any html element
    - most common are `class` and `id`

---

# More about attributes:

- Every attribute has one key (attribute name)
- Every attribute has one value (attribute value) -- usually
- Keys aren't quoted
- An = sign separates the key and value
- Attributes are separated by a space
- Values get wrapped in quotes ""
- Don't duplicate attributes on the same element

---

# HTML document structure & Page hierarchy

In this section:

- relationships between elements
- structure of an html document
- semantics

---

# Nesting

Elements can nest inside one another. The resulting structure is tree-like, creating a hierarchy of relationships. Just as in a family tree, we have ancestors, parents, children, and siblings.

---

# Demo: discuss parent-child relationships here

```html
<section>
  <h2>Rhodesian Ridgeback</h2>
  <p>Rhodesian Ridgebacks are fierce, loyal dogs. Read some facts about them.</p>
  <ul>
    <li>Also known as the African Lion Hound</li>
    <li>Bred as big-game hunting companions</li>
    <li>Adults weigh 70-85 lbs</li>
  </ul>
</section>
```

---

# EXERCISE

https://glitch.com/edit/#!/bears-in-my-html

about 20-30 min

---

### Typical structure

Can you name some sections of an HTML page?

Content of an HTML doc

- `DOCTYPE html` version of html for browser
- `<html>` root element
- document metadata (`link`, `meta`, `title`, `style`) -- "modify the presentation or the behavior of the rest of the document, set up links to other documents, or convey other out of band information."
- `body` only one of these
- header, nav bar, main content, sidebar, footer -- major structural components of the page

---

# Semantic HTML

"Semantic" -- refers to the meaning of something, in linguistics, we are talking about the meanings of words. Semantic html -- html elements that carry some meaning about the content they contain, or indicate their purpose.

---

```html
<section>
  <header>
    <h1>Amazing Dog Stories</h1>
  </header>
  <article>
    <h2>Chihuahua Rescues Owner from Burning Building</h2>
    <p>Lorem ipsum dolor sit amet...</p>
  </article>
</section>

<div>
  <div>
    <div>Amazing Dog Stories</div>
  </div>
  <div>
    <div>Chihuahua Rescues Owner from Burning Building</div>
    <div>Lorem ipsum dolor sit amet...</div>
  </div>
</div>
```

---

# Block vs. inline elements

---

# Common block elements

- Paragraphs (`<p>`)
- Headers (`<h1>` through `<h6>`)
- Divisions (`<div>`)
- Lists and list items (`<ol>`, `<ul>`, and `<li>`)
- Forms (`<form>`)

---

# Common inline elements

- Spans (`<span>`)
- Images (`<img>`)
- Anchors (`<a>`)

---

# `<span>` and `<div>`

- span is inline and div is block
- not semantic
- used to group together some chunk of html content and associate other information with it -- most commonly a class or id attribute for styling or javascript
- as a "container" or a "wrapper"
- useful and will use them often

---

# Lab

https://glitch.com/edit/#!/momentum-w1d1
