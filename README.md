# Backend Branch

## API Usage

### Get a list of restaurants nearby user location

**Endpoint:** "https://makanwhere.pythonanywhere.com/api/nearby/"

**Required input:**
location (this can be a address or postal code)
distance (how far from provided location to show restaurants)

**Results:** A list of 20 restaurants that are within the distance will be returned

**Usage:**

```Javascript
$.ajax({
    type: "POST",
    data: {location: "60 Example Street/545021", distance: "1000"},
    success: function(response){
    	for(var i=0; i<response.length; i++){
    		$("#nearybyRestaurants").append("<li>" + response[i] + "<li>");
    	}
    },
    error: function(response){
    		console.log("Error");
    	}
    }
})
```
