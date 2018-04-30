# Lesson 5.7 Responsive Tables - Contained Scrolling

`div.contained_table { width: 100%; overflow-x: auto; }` This contains the table in the viewport, but allows scrolling within the viewport. Very cool. :ok_hand:

Example code:
```
<style>
	td {
		min-width: 75px;
		text-align: center;
	}
	th:first-of-type {
		min-width: 125px;
	}
	div.contained_table {
		width: 50%;
		overflow-x: auto;
	}
</style>
	  
<body>
	<div class="contained_table">
	  <table>
        <thead>
          <tr>
            <th>Team</th>
            <th>1st</th>
            <th>2nd</th>
            <th>3rd</th>
            <th>4th</th>
            <th>5th</th>
            <th>6th</th>
            <th>7th</th>
            <th>8th</th>
            <th>9th</th>
            <th>Final</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Toronto</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>4</td>
            <td>0</td>
            <td>1</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>5</td>
          </tr>
          <tr>
            <td>San Francisco</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>4</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>0</td>
            <td>4</td>
          </tr>
        </tbody>
      </table>
	</div>
</body>
```
[ND024_Part2_Lesson05_07_contained_scrolling.html](http://htmlpreview.github.io/?https://github.com/genchau/nd024-mws-notes/blob/master/ND024_Part2_Lesson05_07_contained_scrolling.html)

- - -
Next up: [Fonts](ND024_Part2_Lesson05_08.md) or return to [Table Of Contents](./ND024_TableOfContents.md)
