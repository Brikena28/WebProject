var failed_loggin = 0;
			function auth(){
				var email = document.getElementById("email").value;
				var password = document.getElementById("password").value;

				if (email == "" || password == ""){
					failed_loggin++;

					document.getElementById("error").style.display = "block";
					document.getElementById("success").style.display = "none";
				} else {
					document.getElementById("error").style.display = "none";
					document.getElementById("success").style.display = "block";
				}

				if (failed_loggin > 3){
					alert("Too many attemps. Try again in 15 minutes!.")
				}
			}