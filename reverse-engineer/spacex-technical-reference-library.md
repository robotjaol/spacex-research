# SpaceX Technical Reference Library

Katalog sumber teknis publik untuk engineering study, rekonstruksi, dan simulasi. Pemeriksaan: **3 September 2026**.

**30 dokumen dalam 10 kelompok: 23 PDF berhasil dibuka, 7 alamat unduhan masih memerlukan pemeriksaan akses.** Dua sumber HTML tambahan dicantumkan terpisah.

Tanda **†** berarti alamat PDF teridentifikasi melalui indeks, rekaman institusi, atau sitasi, tetapi berkas tidak berhasil dibuka saat pemeriksaan. Ini bukan jaminan bahwa tautannya masih berfungsi. Halaman rekaman disediakan bila tersedia. Alamat FAA `/media/…` dan endpoint `/download` dapat langsung menyajikan PDF meskipun tidak berakhiran `.pdf`.

Nilai **Essential** menunjukkan sumber inti untuk subsistem terkait; **High** menunjukkan detail teknis atau metode yang kuat; **Supporting** menunjukkan konteks, sejarah, atau cakupan teknis terbatas. Penilaian ini adalah kurasi untuk kebutuhan pengguna, bukan pengukuran frekuensi sitasi.

Akses publik tidak otomatis memberikan lisensi open-source. Katalog menyimpan metadata dan tautan; izin pemakaian atau redistribusi setiap dokumen tetap mengikuti ketentuan sumbernya.

## Urutan baca yang disarankan

Mulai dari SX01–SX02 untuk antarmuka Falcon, SX05 dan SX27 untuk kendaraan Starship, SX15 untuk ground systems, SX18 untuk Crew Dragon, dan SX11–SX12 untuk heatshield. Untuk simulasi pendaratan, baca SX09, lalu SX25–SX26. SX10 menjadi contoh rekonstruksi berbasis pengukuran sinyal.

## 1. Falcon 9 dan Falcon Heavy

### SX01. Falcon User’s Guide

- **PDF:** [Unduh PDF](https://www.spacex.com/assets/media/falcon-users-guide-2025-05-09.pdf)
- **Penerbit/institusi:** SpaceX
- **Tahun/versi:** 2025; 9 Mei 2025
- **Teknologi/subsistem:** Falcon 9/Falcon Heavy; struktur, Merlin, avionik, antarmuka payload, lingkungan penerbangan
- **Kegunaan untuk rekonstruksi:** Rujukan awal untuk geometri, batas massa dan volume, antarmuka mekanis, beban, lingkungan termal, serta persyaratan integrasi dan verifikasi payload.
- **Nilai teknis:** Essential
- **Jenis sumber:** Dokumen primer SpaceX
- **Batas penggunaan:** Panduan pelanggan; tidak menyediakan CAD internal, peta mesin lengkap, atau kode penerbangan.
- **Bagian awal yang dibaca:** Bagian 2.3 dan 2.5; bagian lingkungan, antarmuka, serta verifikasi payload.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.spacex.com/vehicles/falcon-9/)

### SX02. Rideshare Payload User’s Guide

- **PDF:** [Unduh PDF](https://storage.googleapis.com/rideshare-static/Rideshare_Payload_Users_Guide.pdf)
- **Penerbit/institusi:** SpaceX
- **Tahun/versi:** 2026; Version 11; sampul Agustus 2026, change log Juli 2026
- **Teknologi/subsistem:** Payload adapter, mekanika, kelistrikan, EMC, deployment, ground support equipment
- **Kegunaan untuk rekonstruksi:** Sangat berguna untuk rekonstruksi antarmuka payload: gambar dimensi, konfigurasi pelat, koneksi listrik, lingkungan getaran, dan metode uji.
- **Nilai teknis:** Essential
- **Jenis sumber:** Dokumen primer SpaceX
- **Batas penggunaan:** URL dapat berubah isinya mengikuti revisi. Sampul dan change log berbeda satu bulan; gunakan nomor versi 11 sebagai identitas utama.
- **Bagian awal yang dibaca:** Bagian 2, 4–7 dan lampiran gambar antarmuka.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.spacex.com/rideshare/)

### SX03. NASA Independent Review Team: SpaceX CRS-7 Accident Investigation Report - Public Summary

- **PDF:** [Unduh PDF](https://www.nasa.gov/sites/default/files/atoms/files/public_summary_nasa_irt_spacex_crs-7_final.pdf)
- **Penerbit/institusi:** NASA
- **Tahun/versi:** 2018; 12 Maret 2018; peristiwa 28 Juni 2015
- **Teknologi/subsistem:** Upper stage Falcon 9; tangki LOX, COPV helium, strut, kualifikasi komponen
- **Kegunaan untuk rekonstruksi:** Menghubungkan konfigurasi perangkat keras, bukti investigasi, dan proses pengujian. Berguna untuk menilai asumsi struktur dan kemungkinan mekanisme kegagalan.
- **Nilai teknis:** Essential
- **Jenis sumber:** Ringkasan investigasi primer NASA
- **Batas penggunaan:** Ringkasan publik, bukan seluruh berkas investigasi. Pertahankan tingkat kepastian masing-masing temuan.
- **Bagian awal yang dibaca:** Bagian investigasi, temuan, dan rekomendasi.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.

## 2. Starship dan Super Heavy

### SX04. Starship User’s Guide

- **PDF:** [Unduh PDF†](https://www.elonx.cz/docs/starship_users_guide_v1.pdf)
- **Penerbit/institusi:** SpaceX; salinan ElonX
- **Tahun/versi:** 2020; Revision 1.0, Maret 2020
- **Teknologi/subsistem:** Starship; payload envelope, konfigurasi misi, antarmuka payload
- **Kegunaan untuk rekonstruksi:** Titik acuan historis untuk membandingkan perubahan geometri, konsep operasi, dan kebutuhan payload Starship.
- **Nilai teknis:** High
- **Jenis sumber:** Dokumen primer SpaceX melalui mirror
- **Batas penggunaan:** Desain pendahuluan tahun 2020; jangan menjadikannya spesifikasi kendaraan yang terbang sekarang.
- **Bagian awal yang dibaca:** Diagram payload dan uraian misi.
- **Status akses:** PDF ditemukan dalam indeks publik, tetapi unduhan tidak berhasil dibuka saat pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.elonx.net/documents/)

### SX05. Final Tiered Environmental Assessment: Starship/Super Heavy Vehicle Increased Cadence at Boca Chica

- **PDF:** [Unduh PDF](https://www.faa.gov/media/94346)
- **Penerbit/institusi:** FAA
- **Tahun/versi:** 2025; April 2025
- **Teknologi/subsistem:** Starship/Super Heavy; dimensi, propelan, mesin, profil penerbangan, fasilitas
- **Kegunaan untuk rekonstruksi:** Bab uraian kegiatan dan tabel kendaraan menyediakan batas konfigurasi, inventaris propelan, serta hubungan kendaraan dengan fasilitas darat.
- **Nilai teknis:** Essential
- **Jenis sumber:** Dokumen primer pemerintah; kajian lingkungan
- **Batas penggunaan:** Sebagian parameter adalah rencana atau batas skenario yang dinilai. Dokumen ini tidak membuktikan konfigurasi aktual setiap penerbangan.
- **Bagian awal yang dibaca:** Chapter 2 dan tabel karakteristik kendaraan.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.faa.gov/space/stakeholder_engagement/spacex_starship)

### SX06. SpaceX Starship SN10 Prototype Safety Analysis: A Case Study on Organization’s Needs Management

- **PDF:** [Unduh PDF](https://www.scielo.br/j/jatm/a/5T94g6Nxj4hdz5jbKk657Sx/?format=pdf&lang=en)
- **Penerbit/institusi:** Journal of Aerospace Technology and Management; Reinhardt dkk.
- **Tahun/versi:** 2024; Volume 16, e3724; DOI 10.1590/jatm.v16.1357
- **Teknologi/subsistem:** SN10; pressurization, system safety, interaksi keputusan desain dan operasi
- **Kegunaan untuk rekonstruksi:** Contoh penerapan STAMP, CAST, dan STPA pada informasi publik SN10; membantu menyusun hipotesis bahaya dan kebutuhan sistem pressurization.
- **Nilai teknis:** Supporting
- **Jenis sumber:** Analisis akademik independen
- **Batas penggunaan:** Analisis berbasis informasi publik dengan fokus keselamatan organisasi; bukan laporan investigasi resmi atau validasi desain internal.
- **Bagian awal yang dibaca:** Model sistem, analisis kausal, dan rekomendasi pressurization.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://doi.org/10.1590/jatm.v16.1357)

## 3. Merlin dan Raptor propulsion

Untuk model mesin yang lebih terperinci, baca **SX27 bagian 2.1.1** tentang Raptor dan **SX01 bagian 2.3** untuk uraian primer propulsi Falcon. Dua sumber berikut melengkapi sejarah arsitektur dan metode perhitungan.

### SX07. Statement of Gwynne Shotwell before the House Armed Services Subcommittee on Strategic Forces

- **PDF:** [Unduh PDF](https://docs.house.gov/meetings/AS/AS29/20150317/103135/HHRG-114-AS29-Wstate-ShotwellG-20150317.pdf)
- **Penerbit/institusi:** SpaceX / U.S. House of Representatives
- **Tahun/versi:** 2015; 17 Maret 2015
- **Teknologi/subsistem:** Merlin 1D; pengujian dan produksi mesin; konsep awal Raptor full-flow staged combustion
- **Kegunaan untuk rekonstruksi:** Sumber primer historis untuk melacak pernyataan SpaceX tentang pilihan siklus Raptor, propelan, reuse, serta pengalaman produksi Merlin.
- **Nilai teknis:** Supporting
- **Jenis sumber:** Kesaksian resmi SpaceX di Kongres
- **Batas penggunaan:** Dokumen kebijakan dengan bagian teknis singkat; tidak memuat desain turbopump atau parameter Raptor produksi.
- **Bagian awal yang dibaca:** Halaman 14 PDF untuk Merlin dan Raptor.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.

### SX08. Computer Program for Calculation of Complex Chemical Equilibrium Compositions and Applications, II: Users Manual and Program Description

- **PDF:** [Unduh PDF](https://rocketcea.readthedocs.io/en/latest/_static/CEA_User_Manual_(NASA_RP-1311).pdf)
- **Penerbit/institusi:** NASA; McBride dan Gordon; mirror RocketCEA
- **Tahun/versi:** 1996; NASA RP-1311, Part II
- **Teknologi/subsistem:** Metode analisis termokimia propelan; relevan untuk LOX/RP-1 dan LOX/metana
- **Kegunaan untuk rekonstruksi:** Dasar perhitungan equilibrium, c*, Isp ideal, dan sensitivitas campuran untuk menguji kewajaran model Merlin/Raptor.
- **Nilai teknis:** High
- **Jenis sumber:** Manual metode NASA; bukan dokumen desain SpaceX
- **Batas penggunaan:** Hasil ideal tidak menentukan efisiensi mesin aktual, geometri injector, cooling channel, atau performa turbopump.
- **Bagian awal yang dibaca:** Format input, rocket performance, contoh perhitungan, dan batas model.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://ntrs.nasa.gov/citations/19960044559)

## 4. Avionics, flight software, telemetry, dan GN&C

Arsitektur avionik Falcon juga dibahas dalam **SX01 bagian 2.5**. Sumber Starlink di bawah membahas komunikasi satelit; penerapannya tidak otomatis berlaku pada telemetri peluncur.

### SX09. Autonomous Precision Landing of Space Rockets

- **PDF:** [Unduh PDF†](https://www.larsblackmore.com/nae_bridge_2016.pdf)
- **Penerbit/institusi:** Lars Blackmore, SpaceX / National Academy of Engineering, The Bridge
- **Tahun/versi:** 2016; Winter 2016, volume 46 nomor 4, halaman 15–20
- **Teknologi/subsistem:** Powered landing; guidance, trajectory optimization, kendala aktuator
- **Kegunaan untuk rekonstruksi:** Penjelasan oleh engineer SpaceX tentang persoalan pendaratan presisi dan optimasi lintasan; membantu merumuskan kebutuhan simulator landing.
- **Nilai teknis:** High
- **Jenis sumber:** Tulisan primer engineer SpaceX
- **Batas penggunaan:** Uraian teknis konseptual; bukan source code atau spesifikasi flight software.
- **Bagian awal yang dibaca:** Formulasi masalah pendaratan dan peran optimasi.
- **Status akses:** Judul dan alamat PDF teridentifikasi; endpoint penulis gagal dibuka saat pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.nae.edu/164334/Autonomous-Precision-Landing-of-Space-Rockets)

### SX10. Signal Structure of the Starlink Ku-Band Downlink

- **PDF:** [Unduh PDF](https://arxiv.org/pdf/2210.11578)
- **Penerbit/institusi:** Humphreys, Iannucci, Komodromos dan Graff; University of Texas at Austin
- **Tahun/versi:** 2022; Preprint 2022; publikasi jurnal IEEE 2023
- **Teknologi/subsistem:** Starlink RF; waveform downlink, OFDM, sinkronisasi, timing
- **Kegunaan untuk rekonstruksi:** Contoh langsung rekonstruksi struktur sinyal dari pengukuran, dengan model yang dapat dibandingkan dengan observasi.
- **Nilai teknis:** Essential
- **Jenis sumber:** Penelitian independen berbasis pengukuran
- **Batas penggunaan:** Membahas downlink Starlink; tidak menyediakan protokol telemetri internal Falcon/Dragon atau akses isi komunikasi pelanggan.
- **Bagian awal yang dibaca:** Struktur frame, sinkronisasi, dan metodologi estimasi.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://arxiv.org/abs/2210.11578)

## 5. Structures, materials, aerodynamics, dan thermal protection

### SX11. Post-Flight Evaluation of PICA and PICA-X: Comparisons of the Stardust SRC and Space-X Dragon 1 Forebody Heatshield Materials

- **PDF:** [Unduh PDF†](https://ntrs.nasa.gov/api/citations/20140005558/downloads/20140005558.pdf)
- **Penerbit/institusi:** NASA Ames; Stackpoole dkk.
- **Tahun/versi:** 2013; Publikasi 2013; rekaman NTRS 20140005558
- **Teknologi/subsistem:** Dragon 1; PICA/PICA-X, ablasi, kondisi material setelah penerbangan
- **Kegunaan untuk rekonstruksi:** Menghubungkan material TPS dengan bukti pascapenerbangan, sehingga lebih kuat untuk studi rekonstruksi daripada asumsi dari foto eksterior saja.
- **Nilai teknis:** Essential
- **Jenis sumber:** Publikasi primer NASA
- **Batas penggunaan:** Konfigurasi dan material Dragon 1 historis; tidak otomatis mewakili seluruh varian Dragon atau TPS Starship.
- **Bagian awal yang dibaca:** Perbandingan material, lokasi sampel, dan evaluasi pascapenerbangan.
- **Status akses:** NTRS mengidentifikasi berkas PDF publik; endpoint unduhan gagal dibuka saat pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://ntrs.nasa.gov/citations/20140005558)

### SX12. A Perspective on the Design and Development of the SpaceX Dragon Spacecraft Heatshield

- **PDF:** [Unduh PDF†](https://uknowledge.uky.edu/cgi/viewcontent.cgi?article=1029&context=ablation)
- **Penerbit/institusi:** Daniel J. Rasky, NASA Ames / 5th Ablation Workshop, University of Kentucky
- **Tahun/versi:** 2012; Keynote, 28 Februari 2012
- **Teknologi/subsistem:** Dragon; pengembangan heatshield dan PICA-X
- **Kegunaan untuk rekonstruksi:** Memberikan konteks teknis keputusan pengembangan, manufaktur, dan pengujian heatshield dari peneliti NASA yang terlibat.
- **Nilai teknis:** High
- **Jenis sumber:** Presentasi primer NASA dalam workshop teknis
- **Batas penggunaan:** Presentasi pengembangan historis, bukan spesifikasi material atau gambar produksi lengkap.
- **Bagian awal yang dibaca:** Riwayat pengembangan, pengujian, dan pilihan material.
- **Status akses:** Rekaman institusi dan tautan unduhan tersedia; PDF gagal dibuka saat pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://uknowledge.uky.edu/ablation/2012/Keynote/1/)

### SX13. Aerothermal Databases and Load Predictions for Retro Propulsion-Assisted Launch Vehicles (RETALT)

- **PDF:** [Unduh PDF](https://elib.dlr.de/148410/1/Laureti-Karl2022_Article_AerothermalDatabasesAndLoadPre.pdf)
- **Penerbit/institusi:** Mariasole Laureti dan Sebastian Karl, DLR / CEAS Space Journal
- **Tahun/versi:** 2022; DOI 10.1007/s12567-021-00413-0
- **Teknologi/subsistem:** Aerothermodynamics, retropropulsion, plume interaction, thermal protection
- **Kegunaan untuk rekonstruksi:** Menjelaskan pembuatan basis data CFD dan estimasi beban panas sepanjang lintasan pada konfigurasi RETALT1 yang menyerupai Falcon 9.
- **Nilai teknis:** High
- **Jenis sumber:** Penelitian metode DLR; kendaraan pembanding
- **Batas penggunaan:** Geometri dan hasil termal RETALT1 tidak boleh dianggap sebagai data Falcon 9.
- **Bagian awal yang dibaca:** Model numerik, matriks CFD, heating pattern, dan sensitivitas turbulensi.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://elib.dlr.de/148410/)

### SX14. Brightness Mitigation Best Practices for Satellite Operators

- **PDF:** [Unduh PDF](https://starlink.com/public-files/BrightnessMitigationBestPracticesSatelliteOperators.pdf)
- **Penerbit/institusi:** SpaceX / Starlink
- **Tahun/versi:** Tanpa tanggal; PDF menyebut workshop 2022; tahun penerbitan tidak dinyatakan
- **Teknologi/subsistem:** Starlink; material optik, pelapis, visors, attitude, pertukaran kebutuhan daya dan termal
- **Kegunaan untuk rekonstruksi:** Uraian primer hubungan antara desain permukaan satelit, refleksi cahaya, penunjukan solar array, dan kendala operasi.
- **Nilai teknis:** High
- **Jenis sumber:** Dokumen primer SpaceX
- **Batas penggunaan:** Berfokus pada mitigasi kecerlangan satelit; bukan data TPS roket. Tahun tidak disimpulkan hanya dari nama workshop.
- **Bagian awal yang dibaca:** Material permukaan, dielectric mirror film, dan teknik pengaturan attitude.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.

## 6. Launch pad, ground systems, dan recovery

### SX15. Written Re-evaluation of the 2022 PEA: Deluge System Operation, Addition of a Forward Heat Shield Interstage, and Expansion of the Area of Potential Effects for Cultural Resources

- **PDF:** [Unduh PDF](https://www.faa.gov/media/72816)
- **Penerbit/institusi:** FAA
- **Tahun/versi:** 2023; November 2023
- **Teknologi/subsistem:** Boca Chica; deluge, water-cooled steel plate, ground systems, hot-stage heat shield
- **Kegunaan untuk rekonstruksi:** Sumber primer bernilai tinggi untuk memahami hubungan pelindung landasan, sistem air, pengoperasian mesin, dan perlindungan interstage.
- **Nilai teknis:** Essential
- **Jenis sumber:** Dokumen primer pemerintah; perubahan konfigurasi untuk perizinan
- **Batas penggunaan:** Menggambarkan perubahan yang dinilai pada 2023; bukan gambar as-built seluruh fasilitas.
- **Bagian awal yang dibaca:** Halaman 2–7 PDF dan deskripsi sistem deluge.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.faa.gov/space/stakeholder_engagement/spacex_starship)

### SX16. Draft Environmental Impact Statement for Authorizing Changes to the Falcon Launch Program at Vandenberg Space Force Base, California

- **PDF:** [Unduh PDF](https://vsfbfalconlauncheis.com/Portals/falconprogrameis/PublicDocuments/VSFB_Falcon_Launch_Draft_EIS_May_2025Rev.pdf)
- **Penerbit/institusi:** U.S. Department of the Air Force / U.S. Space Force
- **Tahun/versi:** 2025; Draft, Mei 2025
- **Teknologi/subsistem:** SLC-4/SLC-6; peluncuran, pendaratan, penyimpanan propelan, infrastruktur Falcon
- **Kegunaan untuk rekonstruksi:** Peta fasilitas dan uraian kegiatan membantu merekonstruksi fungsi pad, alur ground operations, serta skenario launch dan recovery.
- **Nilai teknis:** High
- **Jenis sumber:** Dokumen primer pemerintah; draft EIS
- **Batas penggunaan:** Tetap berstatus draft Mei 2025 dalam katalog ini. Rencana tidak sama dengan persetujuan atau fasilitas yang telah dibangun.
- **Bagian awal yang dibaca:** Uraian proposed action, peta fasilitas, dan profil operasi.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://vsfbfalconlauncheis.com/)

### SX17. Starship/Super Heavy at Kennedy Space Center LC-39A: Final Environmental Impact Statement, Volume I

- **PDF:** [Unduh PDF†](https://www.faa.gov/space/stakeholder_engagement/spacex_starship_ksc/SpaceX-SSH-LC-39A-Final-EIS-Volume-I.pdf)
- **Penerbit/institusi:** FAA
- **Tahun/versi:** 2026; Januari 2026
- **Teknologi/subsistem:** LC-39A; Starship/Super Heavy, pad, propellant infrastructure, launch/landing operations
- **Kegunaan untuk rekonstruksi:** Rujukan utama untuk memetakan rencana fasilitas Starship di KSC, kebutuhan sistem darat, dan batas skenario operasi.
- **Nilai teknis:** Essential
- **Jenis sumber:** Dokumen primer pemerintah; final EIS
- **Batas penggunaan:** Final EIS bukan gambar as-built atau izin tanpa syarat untuk semua skenario yang dibahas.
- **Bagian awal yang dibaca:** Volume I: uraian proyek dan alternatif fasilitas.
- **Status akses:** Tautan PDF dikonfirmasi pada halaman FAA dan rekaman EIS; berkas besar gagal dibuka saat pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.faa.gov/space/stakeholder_engagement/spacex_starship_ksc)

## 7. Dragon dan spacecraft systems

### SX18. Development of the Crew Dragon ECLSS

- **PDF:** [Unduh PDF†](https://ttu-ir.tdl.org/bitstreams/72897181-04f2-4ae2-85b0-569d5acef49d/download)
- **Penerbit/institusi:** Jason Silverman, Andrew Irby dan Theodore Agerton, SpaceX / ICES; repositori Texas Tech University
- **Tahun/versi:** 2020; ICES-2020-333
- **Teknologi/subsistem:** Crew Dragon; environmental control and life support, air revitalization, kelembapan, kontrol atmosfer
- **Kegunaan untuk rekonstruksi:** Paper penulis SpaceX tentang pengembangan ECLSS; berguna untuk memahami arsitektur, pilihan teknologi, integrasi, dan proses verifikasi.
- **Nilai teknis:** Essential
- **Jenis sumber:** Paper konferensi primer SpaceX
- **Batas penggunaan:** Tidak memuat seluruh gambar produksi, software kontrol, atau spesifikasi rinci yang dibutuhkan untuk membangun sistem operasional.
- **Bagian awal yang dibaca:** Pemilihan arsitektur, pengendalian atmosfer, dan program pengujian.
- **Status akses:** Rekaman universitas mencantumkan ICES-2020-333.pdf; unduhan gagal dibuka saat pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://ttu-ir.tdl.org/items/43868cc4-9083-4ca6-b865-d6d3897fb658)

### SX19. International Docking System Standard: Interface Definition Document, Revision F

- **PDF:** [Unduh PDF](https://newspaceeconomy.ca/wp-content/uploads/2024/08/idss_idd_revision_f.pdf)
- **Penerbit/institusi:** Mitra International Docking System Standard; mirror New Space Economy
- **Tahun/versi:** 2022; Revision F, Juli 2022
- **Teknologi/subsistem:** Antarmuka docking; soft capture, hard capture, geometri, beban, kompatibilitas
- **Kegunaan untuk rekonstruksi:** Acuan dimensi dan batas antarmuka untuk studi kompatibilitas docking Dragon dengan ISS; membantu memisahkan antarmuka standar dari mekanisme internal.
- **Nilai teknis:** High
- **Jenis sumber:** Standar teknis antarlembaga melalui mirror
- **Batas penggunaan:** Standar ini tidak mengungkap desain internal docking system Dragon. PDF mirror dipakai karena endpoint resmi tidak berhasil dibuka.
- **Bagian awal yang dibaca:** Gambar antarmuka, capture envelope, dan persyaratan beban.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.internationaldockingstandard.com/)

### SX20. SpaceX Demonstration Mission: Mission Objectives

- **PDF:** [Unduh PDF](https://www.nasa.gov/wp-content/uploads/2015/06/641018main_pk_objectives.pdf)
- **Penerbit/institusi:** NASA / SpaceX
- **Tahun/versi:** 2012; Misi demonstrasi COTS 2/3; tahun mengikuti konteks misi
- **Teknologi/subsistem:** Dragon COTS; rendezvous, relative GPS, LIDAR, komunikasi UHF, abort dan free drift
- **Kegunaan untuk rekonstruksi:** Daftar demonstrasi penerbangan memberi skenario verifikasi yang konkret untuk model rendezvous dan urutan operasi Dragon.
- **Nilai teknis:** Supporting
- **Jenis sumber:** Dokumen misi primer; dua halaman
- **Batas penggunaan:** Daftar tujuan demonstrasi, bukan algoritma GN&C. Tanggal direktori unggahan 2015 bukan tahun misi.
- **Bagian awal yang dibaca:** Tujuan demonstrasi pendekatan ISS dan operasi proximity.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.

## 8. FCC, FAA, NASA, dan government technical documents

Dokumen NASA terdapat pada SX03, SX08, SX11–SX12, dan SX20; dokumen FAA terdapat pada SX05, SX15, dan SX17. Penempatan mengikuti kegunaan teknis utama agar tidak menduplikasi entri.

### SX21. SpaceX Non-Geostationary Satellite System: Attachment A, Technical Information to Supplement Schedule S

- **PDF:** [Unduh PDF†](https://licensing.fcc.gov/myibfs/download.do?attachment_key=1158350)
- **Penerbit/institusi:** Space Exploration Holdings, LLC / filing FCC
- **Tahun/versi:** 2016; SAT-LOA-20161115-00118
- **Teknologi/subsistem:** Starlink awal; orbit, beam, antena, spektrum, parameter jaringan
- **Kegunaan untuk rekonstruksi:** Lampiran teknis pengajuan awal untuk merekonstruksi asumsi konstelasi dan radio, lalu membandingkannya dengan perubahan perizinan berikutnya.
- **Nilai teknis:** High
- **Jenis sumber:** Lampiran teknis primer SpaceX dalam filing regulator
- **Batas penggunaan:** Konfigurasi historis. FCC 18-38 mencatat erratum 22 November 2016 untuk skala kontur antena; verifikasi revisi sebelum mengambil angka atau diagram.
- **Bagian awal yang dibaca:** Parameter sistem dan antena; cocokkan dengan erratum serta Schedule S.
- **Status akses:** Alamat unduhan FCC lama teridentifikasi melalui sitasi; akses endpoint lama belum berhasil diverifikasi.
- **Rekaman/halaman pendamping:** [Buka sumber](https://docs.fcc.gov/public/attachments/FCC-18-38A1.pdf)

### SX22. SpaceX NGSO Satellite System: Memorandum Opinion, Order and Authorization, FCC 18-38

- **PDF:** [Unduh PDF](https://docs.fcc.gov/public/attachments/FCC-18-38A1.pdf)
- **Penerbit/institusi:** FCC
- **Tahun/versi:** 2018; Dirilis 29 Maret 2018
- **Teknologi/subsistem:** Starlink generasi awal; orbit, spektrum, interferensi, persyaratan otorisasi
- **Kegunaan untuk rekonstruksi:** Sumber primer untuk batas rancangan konstelasi yang disetujui dan jejak perubahan terhadap filing awal, termasuk rujukan koreksi lampiran antena.
- **Nilai teknis:** High
- **Jenis sumber:** Keputusan regulator primer
- **Batas penggunaan:** Konfigurasi yang diotorisasi tidak sama dengan konstelasi yang benar-benar dikerahkan; dokumen ini historis.
- **Bagian awal yang dibaca:** Uraian sistem, syarat izin, dan catatan kaki filing.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://www.fcc.gov/document/fcc-authorizes-spacex-provide-broadband-satellite-services)

### SX23. SpaceX Gen2 NGSO Satellite System: Authorization and Order, DA 26-36

- **PDF:** [Unduh PDF](https://docs.fcc.gov/public/attachments/DA-26-36A1.pdf)
- **Penerbit/institusi:** FCC Space Bureau
- **Tahun/versi:** 2026; 9 Januari 2026
- **Teknologi/subsistem:** Starlink Gen2; orbital shells, frekuensi, interferensi, debris mitigation
- **Kegunaan untuk rekonstruksi:** Memberikan parameter dan syarat otorisasi generasi berikutnya untuk dibandingkan dengan filing lama dan model jaringan satelit.
- **Nilai teknis:** High
- **Jenis sumber:** Keputusan regulator primer
- **Batas penggunaan:** Jumlah dan orbit yang diizinkan tidak membuktikan jumlah satelit aktif. Jangan mencampur konfigurasi 2016, 2018, dan 2026.
- **Bagian awal yang dibaca:** Grant, tabel orbital shells, syarat operasi, dan lampiran order.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.

## 9. Patents dan academic research

### SX24. Antenna Modules for Phased Array Antennas

- **PDF:** [Unduh PDF](https://patentimages.storage.googleapis.com/03/b1/aa/2f756b99c8fefd/US11018436.pdf)
- **Penerbit/institusi:** USPTO; assignee Space Exploration Technologies Corp.
- **Tahun/versi:** 2021; US11018436B2; granted 25 Mei 2021
- **Teknologi/subsistem:** Phased-array antenna; modul RF, PCB, integrasi mekanis dan termal
- **Kegunaan untuk rekonstruksi:** Gambar dan klaim mengungkap alternatif susunan modul serta hubungan komponen yang sering sulit ditafsirkan hanya dari foto perangkat.
- **Nilai teknis:** High
- **Jenis sumber:** Paten publik SpaceX
- **Batas penggunaan:** Paten menjelaskan invensi yang diklaim; tidak membuktikan bahwa satu konfigurasi tertentu dipakai dalam produk produksi.
- **Bagian awal yang dibaca:** Gambar, detailed description, claims, dan keluarga paten.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://patents.google.com/patent/US11018436B2/en)

### SX25. Successive Convexification for 6-DoF Mars Rocket Powered Landing with Free-Final-Time

- **PDF:** [Unduh PDF](https://arxiv.org/pdf/1802.03827)
- **Penerbit/institusi:** Michael Szmuk dan Behçet Açıkmeşe, University of Washington / AIAA
- **Tahun/versi:** 2018; AIAA 2018-0617; arXiv 1802.03827
- **Teknologi/subsistem:** Metode GN&C; optimasi pendaratan 6-DoF, kendala thrust, waktu akhir bebas
- **Kegunaan untuk rekonstruksi:** Menyediakan formulasi matematis untuk membangun dan menguji simulator powered landing dengan dinamika dan kendala yang eksplisit.
- **Nilai teknis:** High
- **Jenis sumber:** Paper metode akademik; bukan implementasi SpaceX
- **Batas penggunaan:** Kasus pendaratan Mars; tidak ada dasar untuk menganggap algoritmanya identik dengan flight software Falcon atau Starship.
- **Bagian awal yang dibaca:** Formulasi optimal control, convexification, dan hasil numerik.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://arxiv.org/abs/1802.03827)

### SX26. Generalized hp Pseudospectral Convex Programming for Powered Descent and Landing

- **PDF:** [Unduh PDF](https://elib.dlr.de/118313/1/Generalized_hp_pseudospectral_convex_algorithm_for_powered_descent_and_landing.pdf)
- **Penerbit/institusi:** Marco Sagliano, DLR / AIAA
- **Tahun/versi:** 2018; AIAA 2018-1870
- **Teknologi/subsistem:** Metode GN&C; transkripsi pseudospectral, convex programming, powered descent
- **Kegunaan untuk rekonstruksi:** Pembanding formulasi numerik untuk menilai ketelitian lintasan dan perilaku solver pada studi pendaratan roket.
- **Nilai teknis:** High
- **Jenis sumber:** Paper metode DLR; bukan implementasi SpaceX
- **Batas penggunaan:** Metode umum; keberhasilan kasus numerik tidak memvalidasi pengendali kendaraan SpaceX.
- **Bagian awal yang dibaca:** Transkripsi, kendala, dan kasus uji numerik.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://elib.dlr.de/118313/)

## 10. Reverse-engineering reports dan independent technical analyses

### SX27. Comparison of SpaceX’s Starship with Winged Heavy-Lift Launcher Options for Europe

- **PDF:** [Unduh PDF](https://elib.dlr.de/214509/1/s12567-025-00625-8.pdf)
- **Penerbit/institusi:** Herberhold, Bussler, Sippel dan Wilken, DLR / CEAS Space Journal
- **Tahun/versi:** 2025; Terbit daring 2025; edisi jurnal 2026, volume 18, halaman 121–144
- **Teknologi/subsistem:** Starship/Super Heavy; Raptor, massa, tangki, lintasan, performa dan recovery
- **Kegunaan untuk rekonstruksi:** Salah satu sumber paling sesuai untuk rekonstruksi: membangun model dari data publik, memodelkan Raptor, dan mengkalibrasi lintasan terhadap empat uji terbang awal.
- **Nilai teknis:** Essential
- **Jenis sumber:** Penelitian rekonstruksi independen DLR
- **Batas penggunaan:** Massa, efisiensi, dan parameter internal tertentu merupakan estimasi. Kalibrasi terhadap data publik tidak menjadikannya spesifikasi resmi SpaceX.
- **Bagian awal yang dibaca:** Bagian 2.1.1 untuk Raptor, 2.1.2 untuk tangki/massa, lalu kalibrasi lintasan dan analisis sensitivitas.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://elib.dlr.de/214509/)

### SX28. Multidisciplinary Design Optimization of Reusable Launch Vehicles for Different Propellants and Objectives

- **PDF:** [Unduh PDF](https://elib.dlr.de/141082/1/1.A34944.pdf)
- **Penerbit/institusi:** Dresia dkk.; DLR, RWTH Aachen, UFABC / Journal of Spacecraft and Rockets
- **Tahun/versi:** 2021; DOI 10.2514/1.A34944
- **Teknologi/subsistem:** Reusable launch vehicles; massa, propelan, lintasan ascent/descent, optimasi
- **Kegunaan untuk rekonstruksi:** Menunjukkan cara menghubungkan model massa, propulsi, dan lintasan dalam optimasi kendaraan, termasuk pembandingan dengan Falcon 9.
- **Nilai teknis:** High
- **Jenis sumber:** Penelitian independen dengan pembanding Falcon 9
- **Batas penggunaan:** Sebagian hasil adalah rancangan hasil optimasi; tidak semua angka atau kendaraan dalam paper merepresentasikan Falcon 9.
- **Bagian awal yang dibaca:** Model subsistem, referensi Falcon 9, asumsi, dan sensitivitas tujuan optimasi.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://elib.dlr.de/141082/)

### SX29. Technical Report on Different RLV Return Modes’ Performances

- **PDF:** [Unduh PDF](https://elib.dlr.de/137735/1/FALCon-Deliverable-D21.pdf)
- **Penerbit/institusi:** Sven Stappert, Madalin Simioana dan Martin Sippel; DLR / proyek FALCon, Horizon 2020
- **Tahun/versi:** 2020; Deliverable D2.1; final 19 Oktober 2020
- **Teknologi/subsistem:** Recovery; RTLS, downrange landing, massa propelan, performa dan operasi
- **Kegunaan untuk rekonstruksi:** Laporan rinci untuk membandingkan konsekuensi metode recovery terhadap massa, lintasan, kapasitas payload, dan operasi peluncur reusable.
- **Nilai teknis:** High
- **Jenis sumber:** Laporan teknis independen DLR/EU
- **Batas penggunaan:** FALCon adalah nama proyek Eropa. Model kendaraan dan biaya tidak otomatis merupakan data Falcon 9 milik SpaceX.
- **Bagian awal yang dibaca:** Bab 3–5 dan skenario VTVL.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://elib.dlr.de/137735/)

### SX30. Exploring the “Internet from Space” with Hypatia

- **PDF:** [Unduh PDF](https://bdebopam.github.io/papers/imc2020-hypatia.pdf)
- **Penerbit/institusi:** Kassing dkk., ETH Zürich / ACM Internet Measurement Conference
- **Tahun/versi:** 2020; DOI 10.1145/3419394.3423635
- **Teknologi/subsistem:** Komunikasi satelit; topologi LEO, routing, latency, simulasi jaringan
- **Kegunaan untuk rekonstruksi:** Kerangka simulasi jaringan konstelasi yang dapat dipakai untuk menguji konsekuensi asumsi orbit dan konektivitas pada model Starlink.
- **Nilai teknis:** High
- **Jenis sumber:** Paper simulasi independen; salinan penulis
- **Batas penggunaan:** Model jaringan tidak mengungkap implementasi routing internal atau telemetri kendaraan peluncur SpaceX.
- **Bagian awal yang dibaca:** Metodologi simulasi, konfigurasi konstelasi, dan hasil latency/routing.
- **Status akses:** Respons PDF dan isi dokumen berhasil dibuka pada pemeriksaan.
- **Rekaman/halaman pendamping:** [Buka sumber](https://doi.org/10.1145/3419394.3423635)

## Sumber HTML tambahan

Keduanya bukan PDF. Alamat PDF tidak dibuat-buat untuk sumber yang hanya ditemukan dalam format HTML.

### HTML01. Feeding The Beast: Super Heavy’s Propellant Distribution System

- **Dokumen:** [Buka HTML](https://ringwatchers.com/article/booster-prop-distribution)
- **Penerbit/tahun:** Jax / Ringwatchers; 2023
- **Subsistem:** Super Heavy; distribusi propelan
- **Kegunaan:** Analisis independen yang secara eksplisit dirujuk dalam paper DLR SX27, referensi 24.
- **Nilai teknis:** High
- **Batas:** HTML publik; PDF publik tidak ditemukan. Interpretasi penulis perlu dicocokkan dengan kendaraan dan tanggal observasi.

### HTML02. We are the SpaceX software team, ask us anything!

- **Dokumen:** [Buka HTML](https://www.reddit.com/r/spacex/comments/gxb7j1/we_are_the_spacex_software_team_ask_us_anything/)
- **Penerbit/tahun:** Tim software SpaceX / r/SpaceX; 2020
- **Subsistem:** Flight software, avionik, software engineering
- **Kegunaan:** Sumber pernyataan langsung engineer untuk menelusuri konteks pengembangan perangkat lunak dan mencari rujukan lanjutan.
- **Nilai teknis:** Supporting
- **Batas:** Format tanya jawab HTML, tanpa PDF; bukan spesifikasi avionik atau repositori flight software.

## Bukti pemakaian yang dapat ditelusuri

Katalog ini tidak menyatakan bahwa setiap entri sering digunakan komunitas. Contoh bukti yang ditemukan:

- Keluarga user guide Falcon dan Starship tercantum pada [indeks dokumen ElonX](https://www.elonx.net/documents/).
- Panduan rideshare dibahas oleh [FEDEVEL](https://fedevel.com/blog/spacex-rideshare-payload-users-guide) dan [r/SpaceX](https://www.reddit.com/r/spacex/comments/ezam7o/spacex_rideshare_payload_guide_pdf/). Diskusi tersebut merujuk edisi sebelumnya, bukan khusus versi 11.
- Paper ECLSS memiliki [diskusi khusus komunitas](https://www.reddit.com/r/spacex/comments/i3a8aj/paper_development_of_the_crew_dragon_eclss/).
- Dokumen evaluasi PICA/PICA-X dirujuk dalam [diskusi rekonstruksi heatshield Dragon](https://www.reddit.com/r/spacex/comments/aqqba3/known_and_unknown_information_about_dragons_heat/).
- Paper DLR SX27 mencantumkan Ringwatchers pada referensi 24, written re-evaluation FAA 2023 pada referensi 26, dan Starship Telemetry Extractor pada referensi 36. Ini bukti penggunaan sumber komunitas dalam penelitian engineering; bukan validasi otomatis seluruh kesimpulan sumber tersebut.

## Menggunakan katalog sebagai basis model

Simpan setiap parameter bersama ID sumber, halaman atau tabel, revisi dokumen, kendaraan/flight yang relevan, satuan, serta status bukti: spesifikasi publik, parameter perizinan, pengukuran, atau estimasi. Jangan menggabungkan parameter dari konfigurasi berbeda tanpa catatan.

Untuk dokumen FAA/FCC, catat apakah parameter merupakan rencana, batas analisis, atau kondisi otorisasi. Untuk model independen, pertahankan asumsi dan rentang ketidakpastian. Catat versi dan checksum PDF saat menyimpan salinan yang memang boleh disimpan; URL stabil dapat menunjuk edisi baru.

Dalam pencarian ini belum diperoleh dokumen primer publik yang menyediakan CAD lengkap Merlin/Raptor, firmware flight computer, atau skema avionik lengkap. Sumber metode umum pada SX08, SX13, SX25, dan SX26 melengkapi analisis, tetapi tidak mengungkap implementasi internal SpaceX.

Paper berbayar atau yang hanya menawarkan request full text tidak dimasukkan sebagai PDF publik terverifikasi. Contohnya paper pengembangan parachute Crew Dragon AIAA 2022-2725; akses terbuka ke PDF lengkapnya belum terverifikasi dalam pencarian ini.
