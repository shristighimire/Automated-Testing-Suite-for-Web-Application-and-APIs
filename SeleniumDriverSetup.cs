using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace WebTests
{
    public class SeleniumDriverSetup
    {
        public static IWebDriver GetDriver()
        {
            ChromeOptions options = new ChromeOptions();
            options.AddArguments("start-maximized");
            return new ChromeDriver(options);
        }
    }
}
