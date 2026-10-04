import sys

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# make an api call and store the response
def get_api_response():
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    try:
        r = requests.get(url, timeout=10)
        print(f"Status code: {r.status_code}")
        r.raise_for_status()
        return r
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    response = get_api_response()

    # get the data from the response json
    response_dict = response.json()
    print(f"Total repositories: {response_dict['total_count']}")

    # collect info for visualization
    repo_dicts = response_dict['items']
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        plot_dict = {
            'value':  repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'] 
        }
        plot_dicts.append(plot_dict)

        # print link and description
        print(f"{repo_dict['name']}: {plot_dict['label']}\n{plot_dict['xlink']}\n")

    # make visualization
    my_style = LS('#1f4e79', base_style=LCS)
    my_style.title_font_size = 24
    my_style.label_font_size = 14
    my_style.major_label_font_size = 18

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred Python Projects on Github'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('python_repos.svg')

if __name__ == "__main__":
    main()
