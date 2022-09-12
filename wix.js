$w.onReady(function () {
	$w("#wixForms1").onWixFormSubmitted( ({fields}) => {
		let url = <deployed url, eg: "https:localhost:8000/api/result">
		let res = []
		let data = { }
		for (let i=0; i < fields.length; i++) {
			res.push(fields[i].fieldValue)
		}	
		for (let i = 0; i < res.length; i++){
			data["soil" + (i+1)] = res[i]
		}
		
		fetch(url, {
          method: 'POST',
		  headers: {
                'Content-Type': 'application/json'
           },
           body: JSON.stringify(data)
		   }).then( (res)  => {
			   return res.json()
			}).then( ( { result} ) => {
				let arr = result.suitableCrops.toString().split(',')
				let str = "We have detected that your soil is: " + result.soil + " \n" + "The best crops to plant based off of your soil composition are: \n \n 🍏🍊🍉🌽🥬🥦 \n \n"
				for (let i=0; i < arr.length; i++){
					str = str + " " + arr[i]
				}
				$w('#text69').text = str
				for (let i = 0; i < result.suitableCrops.length; i++){
						console.log(result.suitableCrops[i])
					}
   })	
})
})
