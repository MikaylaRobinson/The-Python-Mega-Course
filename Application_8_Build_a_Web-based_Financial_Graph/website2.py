from flask import Flask, render_template

app=Flask(__name__)

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.models.annotations import Title
    from bokeh.embed import components 
    from bokeh.resources import CDN

    # Collecting stock data to visualize
    start = datetime.datetime(2015, 11, 1)
    end = datetime.datetime (2016, 3, 10)
    df = data.DataReader(name= "GOOG", data_source = "iex", start = start, end = end)
    df.index = df.index.map(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))

    # Creating series for days the price increased or decreased
    data_increase = df.index[df.close > df.open]
    data_decrease = df.index[df.close < df.open]

    # Creating a new column in the dataframe for increase vs. decrease days 
    def inc_or_dec(c,o):
        if c > o:
            value = "Increase"
        elif c < o:
            value = "Decrease"
        else:
            value = "Equal"
        return value
    df["status"] = [inc_or_dec(c, o) for c, o in zip(df.close, df.open)]

    # Creating a column to define the y-axis
    df["middle"] = (df.open + df.close)/2

    # Creating a column to define the height
    df["height"] = abs(df.close - df.open)

    # Creating the candlestick chart
    p = figure(x_axis_type = "datetime", width = 1000, height = 300, sizing_mode = "scale_width")
    t = Title()
    t.text = "Candlestick Chart"
    p.title = t
    p.grid.grid_line_alpha = 0.4

    # 12 hours in milliseconds 
    hours_12 = 12 * 60 * 60 * 1000

    # Plotting the lines behind the rectangles that show the low and high values for each day
    p.segment(df.index, df.high, df.index, df.low, color= "Black")

    # Plotting the rectangles for the days where the price increased
    p.rect(df.index[df.status == "Increase"],
           df.middle[df.status == "Increase"],
           hours_12,
           df.height[df.status == "Increase"],
           fill_color="#CCFFFF",
           line_color="black")

    # Plotting rectangles for the days the price decreased
    p.rect(df.index[df.status == "Decrease"],
           df.middle[df.status == "Decrease"],
           hours_12,
           df.height[df.status == "Decrease"],
           fill_color="#FF3333",
           line_color="black")

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]

    cdn_js[0]
    cdn_css[0]
    return render_template("plot.j2",
    script1 = script1,
    div1 = div1,
    cdn_css = cdn_css,
    cdn_js = cdn_js)

@app.route('/')
def home():
    return render_template("homepage2.j2")

@app.route('/about/')
def about():
    return render_template("aboutpage2.j2")

if __name__=="__main__":
    app.run(debug=True)