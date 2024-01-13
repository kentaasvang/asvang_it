<script>
	import logoWhite from "$lib/assets/logo/logo-white.svg";
</script>

<svelte:head>
	<title>Asvang IT</title>
	<meta name="asvang-it.no" content="Business home page for asvang-it.no" />
</svelte:head>

<section>
	<!-- Responsive navbar-->
	<nav class="navbar navbar-expand-lg asvang-text-light asvang-bg-dark">
		<div class="container px-5">

			<a class="navbar-brand asvang-text-light" href="/">
				<img src="{logoWhite}" width="40" height="40" alt="">
				Åsvang IT
			</a>

		</div>
	</nav>

	<!-- Header-->
	<header class="asvang-bg-dark py-5">
		<div class="container px-5">
			<div class="row gx-5 justify-content-center">
				<div class="col-lg-6">
					<div class="text-center my-5">

						<h1 class="display-5 fw-bolder asvang-text-light mb-2">
							Konsulenttjenester innen IT-drift og utvikling for små aktører
						</h1>
					</div>
				</div>
			</div>
		</div>
	</header>

	<!-- Features section-->
	<section class="py-5 border-bottom" id="features">
		<div class="container px-5 my-5">
			<div class="row gx-5">

				<div class="col-lg-6 mb-5 mb-lg-0">

					<div class="feature asvang-bg-primary bg-gradient asvang-text-light rounded-3 mb-3">
						<i class="bi bi-wordpress"></i>
					</div>

					<h2 class="h4 fw-bolder">Wordpress</h2>
					<p>
						Vi tilbyr komplette WordPress-løsninger spesialdesignet for små aktører. 
						Vår service inkluderer alt fra skreddersydd design og funksjonalitet, 
						til optimalisering for søkemotorer og sikkerhetstiltak. 
						Med vår ekspertise kan du forvente en høykvalitets, kostnadseffektiv 
						og skalerbar nettløsning som møter dine unike forretningsbehov.
					</p>
				</div>

			</div>
		</div>
	</section>

	<!-- Testimonials section-->
	<section class="py-5 border-bottom asvang-bg-dark">
		<div class="container px-5 my-5 px-5">
			<div class="text-center mb-5">
				<h2 class="fw-bolder asvang-text-light">Tilbakemeldinger fra kunder</h2>
				<p class="lead mb-0 asvang-text-light"></p>
			</div>
			<div class="row gx-5 justify-content-center">
				<div class="col-lg-6">

					<!-- Testimonial -->
					<div class="card mb-4">

						<div class="card-body p-4">

							<div class="d-flex">

								<div class="flex-shrink-0">
									<i class="bi bi-chat-right-quote-fill asvang-text-primary fs-1">
									</i>
								</div>

								<div class="ms-4">

									<p class="mb-1"><s>Skrypt</s> Asvang IT utførte jobben raskt, slik vi ønsket og til en god pris. God kommunikasjon underveis. Vil bruke de igjen.</p>

									<div class="small text-muted">-  Helge Slettingdalen</div>

								</div>

							</div>

						</div>

					</div> <!-- End Testimonial -->

				</div>
			</div>
		</div>
	</section>

	<!-- Contact section-->
	<section class="asvang-bg-light py-5">
		<div class="container px-5 my-5 px-5">
			<div class="text-center mb-5">

				<div class="feature asvang-bg-primary bg-gradient asvang-text-light rounded-3 mb-3">
					<i class="bi bi-envelope"></i>
				</div>

				<h2 class="fw-bolder asvang-text-dark">Ta kontakt!</h2>

				<p class="lead mb-0 asvang-text-dark">
					Send mail til <a href="mailto:post@asvang-it.no">post@asvang-it.no</a>
				</p>

			</div>

		</div>
	</section> 

	<!-- Footer-->
	<footer class="py-5 asvang-bg-dark">
		<div class="container px-5"><p class="m-0 text-center asvang-text-light">Copyright &copy; Asvang IT 2024</p></div>
	</footer>

	<!-- Bootstrap core JS-->
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</section>

<style>
</style>
