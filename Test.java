import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Test {
    public static void main(String[] args){
        System.setProperty("webdriver.chrome.driver", "C:/Users/User/Desktop/selenium/chromedriver.exe");

// 브라우저 실행
        WebDriver driver = new ChromeDriver();

// 구글 홈페이지로 이동
        driver.get("http://www.google.com");
    }
}
