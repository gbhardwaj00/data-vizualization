import requests
import pygal
from pygal.style import Style

from operator import itemgetter

# make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code: ", r.status_code)

# process info for each submission
submission_ids = r.json()
submission_dicts = []

for sid in submission_ids[:30]:
    # make a separate API call for each sid
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(sid) + '.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(sid),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion Link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])

# make visualization

my_style = Style(
    background='#fafaf7',
    plot_background='#fafaf7',
    foreground='#4a4a4a',          # axis labels
    foreground_strong='#1a1a1a',   # title
    foreground_subtle='#e4e4de',   # recessive grid lines
    colors=('#2a6f97',),           # single series -> single hue
    font_family='Helvetica, Arial, sans-serif',
    title_font_size=22,
    label_font_size=12,
    major_label_font_size=12,
    tooltip_font_size=14,
)

my_config = pygal.Config()
my_config.show_legend = False
my_config.x_label_rotation = 45
my_config.truncate_label = 15
my_config.show_y_guides = True
my_config.width = 1000
my_config.height = 800
my_config.print_values = False

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Hacker News: Top 30 Stories by Comment Count'
chart.x_labels = [d['title'] for d in submission_dicts]
chart.add('', [
    {'value': d['comments'], 'label': d['title'], 'xlink': d['link']}
    for d in submission_dicts
])

chart.render_to_file('hn_top_comments.svg')