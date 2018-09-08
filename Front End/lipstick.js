Module.register("lipstick", {
	
	defaults: {
		text = ""
		timeInterval = 1000
	},

	getRecommendation: function(){
		fso = new ActiveXObject("Scripting.FileSystemObject")
		Set ts = fso.OpenTextFile("/pi/Desktop/qsw.txt", ForReading)
		recommendation = ts.ReadAll
		ts.close()
		Set ts1 = fso.OpenTextFile("/pi/Desktop/qsw.txt", ForWriting)
		for(var i = 0; i < ts1.length; i++)(
			ts1.WriteLine("")
		)
		ts1.close()
		return recommendation
	},

	getDom: function(){
		
		var recommendationText = this.getRecommendation():
		var recommendation = document.createTextnode(recommendationText);
		var wrapper = document.createElement("div");
		wrapper.className = this.config.classes ? this.config.classes : "thin xlarge bright";
		wrapper.appendChild(compliment);

		return wrapper;
	}


}
)