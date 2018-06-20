<!DOCTYPE html>
<html>
	<head>
		<title>Submitted Advertisments</title>
		<style>
			.flex-container {
				display: flex;
				flex-direction: row;
			}
			.sidebar{
				width: 200px;
			}
		</style>
	</head>
	<body>
		<p>| <a href="/">Submit a new advertisement for review</a> |</p>
			
		<br>
			{% if page_data['need_previous'] %}
				<a href="/last/{{page_data['context']['first']}}/{{page_data['page_num']}}">Previous</a>
			{% endif %}
			{% if page_data['context']['last'] %}
				<a href="/next/{{page_data['context']['last']}}/{{page_data['page_num']}}">Next</a>
			{% endif %}
		<br>
		<h1>Advertisements submitted for review</h1>
		<div class="flex-container">
			<div class="sidebar"></div>
			<div>
				{% for ad in page_data['context']['items'] %}
					<h2><a href="/reviews/{{ad.id}}">{{ad.url}} </a><small class="alert alrt-info">${{ad.score}}</small> </h2>
					{% if ad.mine %}
					<p><a href="edit/{{ad.id}}">Edit</a> | <a href="delete/{{ad.id}}">Delete</a></p>
					{% endif %}
					<img src="{{ url_for('static', filename=ad.image_url) }}" alt="ad image">
					<p>{{ad.description}}</p>
				{% endfor %}
			</div>
		</div>
		<br>
		{% if page_data['need_previous'] %}
			<a href="/last/{{page_data['context']['first']}}/{{page_data['page_num']}}">Previous</a>
		{% endif %}
		{% if page_data['context']['last'] %}
			<a href="/next/{{page_data['context']['last']}}/{{page_data['page_num']}}">Next</a>
		{% endif %}
	</body>
</html>