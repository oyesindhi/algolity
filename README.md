# Algolity for AlgoTest.in

When we download any backtest's trade report from www.algotest.in, there are things one might not need.
One such thing for me was separating individual leg wise profits rows and profits of a whole trade rows.
I wanted to separate leg wise rows details from main trade row to analyze further.

# Use the app at https://algolity.streamlit.app

Below image is of the raw backtest report that shows both main profit row & leg wise profits combined.

![image](https://user-images.githubusercontent.com/78555897/220935284-e6ae5386-5e51-4d5b-906b-91a9e3dd9a01.png)

So, I built the utility to separate them both.

# Sepearting as per main trades

Below image shows trade being separated on main trade basis
![image](https://user-images.githubusercontent.com/78555897/220935302-834b3197-3b64-49c9-9cfc-47c84c8283ad.png)


# Seperating as per leg wise trades

Below image shows trade being separated on leg wise trade basis
![image](https://user-images.githubusercontent.com/78555897/220936674-3afccf6f-0848-41b0-9b85-57b35e4b17a5.png)

# How to use ?

1. visit https://algolity.streamlit.app, you will see a window like this.
![image](https://user-images.githubusercontent.com/78555897/220943910-a96992c8-dd1f-4147-b20b-6f6743ebc7f7.png)

2. Convert the backtest trade report you downloaded from algotest.in into excel format (XLSX only).
3. Upload the report and voila, you can even download the new segregated report now.

![image](https://user-images.githubusercontent.com/78555897/220944573-874f8aa8-7f4a-4067-bcf0-04f3c8b9c97d.png)


# Credits

I have created this app using python with streamlit.

# Note

If you think we can make it more better by adding some features, please feel free to DM on twitter.

<a href="https://twitter.com/oyesindhi_?ref_src=twsrc%5Etfw" class="twitter-follow-button" data-size="large" data-show-count="false">Follow @oyesindhi_</a>
