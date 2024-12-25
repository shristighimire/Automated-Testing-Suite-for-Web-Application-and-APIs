using NUnit.Framework;
using RestSharp;

namespace ApiTests
{
    [TestFixture]
    public class ApiTests
    {
        private RestClient client;

        [SetUp]
        public void SetUp()
        {
            client = new RestClient("https://api.example.com");  // Replace with your API URL
        }

        [Test]
        public void TestApiResponse()
        {
            var request = new RestRequest("/endpoint", Method.GET);
            var response = client.Execute(request);

            Assert.AreEqual(200, (int)response.StatusCode);
            Assert.IsTrue(response.Content.Contains("expected value"));
        }

        [Test]
        public void TestApiPostRequest()
        {
            var request = new RestRequest("/endpoint", Method.POST);
            request.AddJsonBody(new { name = "test" });
            var response = client.Execute(request);

            Assert.AreEqual(201, (int)response.StatusCode);
        }
    }
}
