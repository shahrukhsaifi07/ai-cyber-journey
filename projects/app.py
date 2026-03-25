from flask import Flask, request,render_template
from scanner import port_scanner
from log_analyzer import analyze_logs
from brute_force import run_brute_force
from ai_analyzer import analyze_with_ai
from agent import security_agent

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")
    # return """ 
    # <h1>Security ToolKit</h1>
    # <h3>Tools:</h3>
    # <form action="/scan" method="post">
    #     Port Scanner:
    #     <input type="text" name="target" placeholder="http://exmple.com">
    #     <input type="submit" value="Scan">
    # </form>
    # <br>
     
    # <a href="/logs">Analyze Logs</a><br><br>
    # <a href="/brute">Brute Force</a>
    # """

@app.route("/scan", methods=["POST"])
def scan():
     target= request.form.get("target")
     results=port_scanner(target)
    #  output="<h2>Open Ports:</h2>"
    #  for port in results:
    #      output +=f"<p>{port}</p>"
    #  return output
     return render_template("scan.html",results=results)

@app.route("/logs")
def logs():
    result = analyze_logs()
    # ai_result=analyze_with_ai(result)
    agent_output=security_agent(result)
    return render_template("logs.html",result=result,agent=agent_output)

    # if isinstance(result, str):
    #     return result

    # output = "<h2>Log Analysis</h2>"
    # output += f"<p>Failed Attempts: {result['failed']}</p>"
    # output += f"<p>Successful Logins: {result['success']}</p>"

    # output += "<h3>User Attempts:</h3>"

    # for user, count in result["users"].items():
    #     output += f"<p>{user} → {count} failed attempts</p>"

    #     if count >= 3:
    #         output += f"<p style='color:red;'> ALERT: {user} under attack!</p>"

    # return output

@app.route("/brute",methods=["GET","POST"])
def brute():
    # if request.method == "GET":
        # return """ 
        # <h2>Brute Force Tool</h2>
        #  <form method="post">
        #     URL: <input type="text" name="url" placeholder="http://example.com/login"><br><br>
        #     Username: <input type="text" name="username"><br><br>
        #     <input type="submit" value="Start Attack">
        # </form>
        # <br>
        # <a href="/">Back</a>
        # """ 
    if request.method =="POST":
        url=request.form.get("url")
        username=request.form.get("username")
        results=run_brute_force(url,username)
        return render_template("brute.html",results=results)
    return render_template("brute.html")

        # output="<h2>📊 Results</h2>"
        # for r in results:
        #     if "FOUND" in r:
        #         output+=f"<p style='color:green;'>{r}</p>"
        #     elif "Error" in r or "not found" in r:
        #         output += f"<p style='color:red;'>{r}</p>"
        #     else:
        #         output += f"<p>{r}</p>"

        # output+="<br><a href='/'>Back To Home</a>"

        # return output



if __name__ =="__main__":
    app.run(debug=True)