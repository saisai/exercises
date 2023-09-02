https://www.queness.com/post/112/a-really-simple-jquery-plugin-tutorial

1. Introduction
Creating a jQuery Plugin is an advanced topic for a jQuery beginner. This month, I have been playing with jQuery intensively. Though I have learnt how to separate the javascript code from html document, I ain't satisfy yet. Whenever I look at my javascript file, it's messy. So, I have decided to go one step further - learn how to write a jQuery plugin to tidy up the javascript file.

This plugin is based on my previous tutorial - Navigation List menu + jQuery Animate Effect Tutorial . Last time, I wrote the script and chucked in all the code in the document.ready section, like this:

$(document).ready(function() {
	
	$('ul#menu li:even').addClass('even');
		
	$('ul#menu li a').mouseover(function() {
		
		$(this).animate( { paddingLeft:"20px" }, { queue:false, duration:500 });
		
	}).mouseout(function() {
	
		$(this).animate( { paddingLeft:"0" }, { queue:true, duration:500 });
		
	}).click(function() {
	
		$(this).animate( { fontSize:"20px" }, { queue:false, duration:500 });
	});
			
});	  

But now, I want it to display something like this:
$(document).ready(function() {
	
	$(#menu).animateMenu({
		padding:20
	})
			
});	  
It looks much more better, and easier to reuse this script for another project.

 

2. Plugin Structure
jQuery website has provided a very detailed explanation in Plugins/Authoring page. However, I found it's hard to understand.

Alright, to make your life easier, I did some research online, the following snippet will be a good structure to write a plugin.

//You need an anonymous function to wrap around your function to avoid conflict
(function($){

	//Attach this new method to jQuery
 	$.fn.extend({ 
 		
 		//This is where you write your plugin's name
 		pluginname: function() {

			//Iterate over the current set of matched elements
    		return this.each(function() {
			
				//code to be inserted here
			
    		});
    	}
	});
	
//pass jQuery to the function, 
//So that we will able to use any valid Javascript variable name 
//to replace "$" SIGN. But, we'll stick to $ (I like dollar sign: ) )		
})(jQuery);

 

2. Plugin With Options
If you look at step one - Introduction, the "padding" value for this plugin is user configurable. It good to have some settings so that user able to chage it according to their own needs. Please make sure you specify the default values for each of the variables for good practise. Now, you'll need the following code:

(function($){

 	$.fn.extend({ 
 		
		//pass the options variable to the function
 		pluginname: function(options) {


			//Set the default values, use comma to separate the settings, example:
			var defaults = {
				padding: 20,
				mouseOverColor : '#000000',
				mouseOutColor : '#ffffff'
			}
				
			var options =  $.extend(defaults, options);

    		return this.each(function() {
				var o = options;
				
				//code to be inserted here
				//you can access the value like this
				alert(o.padding);
			
    		});
    	}
	});
	
})(jQuery);

 

3. The animateMenu Plugin
Now you have learnt the plugin structure. The following is the plugin I created based on my previous tutorial. I have successfull convert the standard jQuery script to a plugin that accepts 4 configurations:

animatePadding : Set the padding value for the animate effect
defaultPadding : Set the default padding value
evenColor : Set the color this color if index value is even number
oddColor : Set the color this color if index value is odd number
(function($){
	$.fn.extend({ 
		//plugin name - animatemenu
		animateMenu: function(options) {

			//Settings list and the default values
			var defaults = {
				animatePadding: 60,
				defaultPadding: 10,
				evenColor: '#ccc',
				oddColor: '#eee'
			};
			
			var options = $.extend(defaults, options);
		
    		return this.each(function() {
				var o =options;
				
				//Assign current element to variable, in this case is UL element
				var obj = $(this);				
				
				//Get all LI in the UL
				var items = $("li", obj);
				  
				//Change the color according to odd and even rows
				$("li:even", obj).css('background-color', o.evenColor);				
			 	$("li:odd", obj).css('background-color', o.oddColor);					  
				  
				//Attach mouseover and mouseout event to the LI  
				items.mouseover(function() {
					$(this).animate({paddingLeft: o.animatePadding}, 300);
					
				}).mouseout(function() {
					$(this).animate({paddingLeft: o.defaultPadding}, 300);
				});
				
    		});
    	}
	});
})(jQuery);


 

4. Full source code
You can save the plugin in a separated file (for example, jquery.animatemenu.js). In this tutorial, I put the script in the html document.

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
    
<head>
    <title></title>
    <script type="text/javascript" src="http://code.jquery.com/jquery-latest.js"></script>
	<script>

(function($){
 	$.fn.extend({ 
 		//plugin name - animatemenu
 		animateMenu: function(options) {

			var defaults = {
			    animatePadding: 60,
           		defaultPadding: 10,
           		evenColor: '#ccc',
           		oddColor: '#eee',
			};
			
			var options = $.extend(defaults, options);
		
    		return this.each(function() {
				  var o =options;
				  var obj = $(this);				
				  var items = $("li", obj);
				  
				  $("li:even", obj).css('background-color', o.evenColor);				
				  $("li:odd", obj).css('background-color', o.oddColor);					  
				  
				  items.mouseover(function() {
					  $(this).animate({paddingLeft: o.animatePadding}, 300);
					
				  }).mouseout(function() {
					  $(this).animate({paddingLeft: o.defaultPadding}, 300);
					
				  });
    		});
    	}
	});
})(jQuery);
	
	</script>
	
	<script type="text/javascript">
	$(document).ready(function() {
		$('#menu').animateMenu({animatePadding: 30, defaultPadding:10});
	});	
	</script>
	<style>
	  body {font-family:arial;font-style:bold}
	  a {color:#666; text-decoration:none}
		#menu {list-style:none;width:160px;padding-left:10px;}
		#menu li {margin:0;padding:5px;cursor:hand;cursor:pointer}
	</style>
</head>   
<body>

<ul id="menu">
	<li>Home</li>
	<li>Posts</li>
	<li>About</li>
	<li>Contact</li>
</ul>

</body>
</html>
 


I hope this tutorial will give you a better understanding. It isn't too hard at all to create a jQuery plugin. I was reluctantly to learn at first, but now, I realized how simple it is.

I will be publishing another tutorial soon - How to create a simple Accordion jQuery Plugin. So, stay tuned.