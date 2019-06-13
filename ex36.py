import json

data = [json.loads(line) for line in open('info.json').readlines()]
result = {}

for person in data:
    birthday_month = person['birthday'][:2]
    if birthday_month == '01':
        birthday_month = 'January'
    elif birthday_month == '02':
        birthday_month = 'February'
    elif birthday_month == '03':
        birthday_month = 'March'
    elif birthday_month == '04':
        birthday_month = 'April'
    elif birthday_month == '05':
        birthday_month = 'May'
    elif birthday_month == '06':
        birthday_month = 'June'
    elif birthday_month == '07':
        birthday_month = 'July'
    elif birthday_month == '08':
        birthday_month = 'August'
    elif birthday_month == '09':
        birthday_month = 'September'
    elif birthday_month == '10':
        birthday_month = 'October'
    elif birthday_month == '11':
        birthday_month = 'November'
    elif birthday_month == '12':
        birthday_month = 'December'
    if birthday_month in result:
        result[birthday_month] += 1
    else:
        result[birthday_month] = 1

print(result)

import numpy as np
import scipy.special

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

def make_plot(title, hist, edges, x, pdf, cdf):
    p = figure(title=title, tools='', background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5)
    p.line(x, pdf, line_color="#ff8888", line_width=4, alpha=0.7, legend="PDF")
    p.line(x, cdf, line_color="orange", line_width=2, alpha=0.7, legend="CDF")

    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'Months'
    p.yaxis.axis_label = 'Frequency'
    p.grid.grid_line_color="white"
    return p

# Normal Distribution

mu, sigma = 0, 0.5

measured = np.random.normal(mu, sigma, 1000)
hist, edges = np.histogram(measured, density=True, bins=50)

x = np.linspace(-2, 2, 1000)
pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))
cdf = (1+scipy.special.erf((x-mu)/np.sqrt(2*sigma**2)))/2

p1 = make_plot("Frequency vs Birthdays", hist, edges, x, pdf, cdf)
output_file('histogram.html', title="histogram.py example")

show(gridplot([p1], ncols=2, plot_width=400, plot_height=400, toolbar_location=None))
