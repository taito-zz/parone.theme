window.onload=autoPOP;

function autoPOP()
{
	var x = document.getElementsByTagName('a');
	for (var i=0;i<x.length;i++)
	{
		if (x[i].getAttribute('className') == 'popup' || x[i].getAttribute('class') == 'popup')
		{
			x[i].onclick = function () {
			return winOpen(this.href)
			}
			x[i].title += 'Open with different window.';
		}
	}
};

function winOpen(url) {
	window.open(
		url,
		'popup',
		'width=718,height=470,scrollbars=0,resizable=1'
	);

	return false;
};

