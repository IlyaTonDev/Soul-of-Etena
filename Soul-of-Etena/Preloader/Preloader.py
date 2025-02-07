<template>
	<div class="loader-section js-loader">
		<div class="loader-section__wrapper">
			<div class="loader-section__img">
				<div class="loader-section__img-wrapper js-loader-img">
					<svg>Картинка загрузки</svg>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
var maxHeight = 178; // Максимальная высота изображения в пикселях
		var images = $('img');
		var loadedImages = 0;

		function updateProgress() {
			var totalImages = images.length;
			var pageLoadPercentage = (loadedImages / totalImages) * 100;
			var heightInPixels = (pageLoadPercentage / 100) * maxHeight;
			$('.js-loader-img').css('max-height', heightInPixels + 'px');
		}

		images.each(function() {
			if (this.complete) {
				loadedImages++;
				updateProgress();
			} else {
				$(this).on('load', function() {
					loadedImages++;
					updateProgress();
				}).on('error', function() {
					loadedImages++;
					updateProgress();
				});
			}
		});

</script>

<style>
.loader-section{
	background: #1F120F;
	color: $white;
	position: fixed;
	z-index: 1000;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;

	&::before{
		content: "";
		display: block;
		width: 100%;
		height: 100%;
		transform: rotate(-19.519deg);
		flex-shrink: 0;
		border-radius: 1307.402px;
		opacity: 0.7;
		background: #1F120F;
		filter: blur(193.34909057617188px);
		position: absolute;
		top: 0;
		left: 0;
		z-index: -1;
	}

	&__bg{
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		z-index: 0;
		object-fit: cover;
		display: block;

		animation: loaderBg 15s linear infinite;

		
	}

	&__wrapper{
		display: flex;
		justify-content: center;
		align-items: center;
		width: 100%;
		height: 100%;
		position: relative;
		z-index: 3;
	}

	&__img{
		height: 178px;
		display: flex;
		flex-direction: column;
		justify-content: flex-end;
		
		&-wrapper{
			max-height: 0;
			height: 178px;
			width: 141px;
			overflow: hidden;
			transition: all 0.5s ease;
			position: relative;
		}

		svg,
		img{
			overflow: hidden;
			width: 141px;
			height: 178px;
			object-position: 50% 100%;
			display: block;
			position: absolute;
			bottom: 0;
			left: 0;	
			object-fit: cover;
		}
	}
}

@keyframes loaderBg {
	0%{
		transform: scale(1)
	}
	50%{
		transform: scale(1.1);
	}
	100%{
		transform: scale(1);
	}
}
</style>
