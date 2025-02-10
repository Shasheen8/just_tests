import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
public void login(HttpServletRequest request, String username, String password) {
  // perform authentication
  boolean isAuthenticated = performAuthentication(username, password);


nano ~/.zshrc

export FALCON_CLIENT_ID=""
export FALCON_CLIENT_SECRET=""

cat ~/.zshrc

source ~/.zshrc
