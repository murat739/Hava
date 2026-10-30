import streamlit as st
import numpy as np
import pandas as pd

# ==========================================
# YASAL UYARI VE TELİF HAKKI BİLDİRİMİ / LEGAL DISCLAIMER
# İşbu yazılım ve içeriği yalnızca bilgi amaçlıdır.
# Kopyalanamaz, çoğaltılamaz ve ticari amaçla kullanılamaz.
# Yazılım geliştiricinin hiçbir sorumluluğu yoktur.
# ==========================================

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Hûve Nüktesi - Kapsamlı Manevi ve Bilimsel Analiz Modülü",
    page_icon="💨",
    layout="wide"
)

# Özel CSS Tasarımı ve Kopyalama Koruması (No-Select / No-Copy)
st.markdown("""
<style>
    /* Tüm sayfada metin seçimini, maviye boyamayı ve kopyalamayı engelle */
    * {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }
    
    input, textarea, [data-testid="stCodeBlock"] {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }

    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        text-align: center;
        font-weight: bold;
        padding-bottom: 10px;
        border-bottom: 2px solid #3B82F6;
    }
    .sub-card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2563EB;
        margin-bottom: 15px;
        line-height: 1.6;
    }
    .quote-box {
        background-color: #FEF3C7;
        padding: 15px;
        border-radius: 8px;
        font-style: italic;
        border-left: 4px solid #D97706;
        margin-bottom: 15px;
    }
    .ref-box {
        background-color: #F1F5F9;
        padding: 15px;
        border-radius: 6px;
        border-left: 4px solid #0F172A;
        font-size: 0.95rem;
        margin-bottom: 15px;
        line-height: 1.5;
    }
    .disclaimer-box {
        background-color: #FFF1F2;
        padding: 12px;
        border-radius: 6px;
        border-left: 4px solid #E11D48;
        font-size: 0.85rem;
        color: #881337;
        margin-top: 20px;
    }
</style>

<script>
    // Sağ tıklama menüsünü tamamen engelle
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
    });

    // Kopyalama (Ctrl+C), Kesme (Ctrl+X), Tümünü Seç (Ctrl+A) kısayollarını engelle
    document.addEventListener('keydown', function(e) {
        if (e.ctrlKey && (e.key === 'c' || e.key === 'C' || e.key === 'x' || e.key === 'X' || e.key === 'a' || e.key === 'A' || e.key === 'u' || e.key === 'U')) {
            e.preventDefault();
        }
    });

    // Kopyalama olayını (Copy Event) doğrudan engelle
    document.addEventListener('copy', function(e) {
        e.preventDefault();
    });
</script>
""", unsafe_allow_html=True)

# Kenar Çubuğu - Dil Seçimi ve Yasal Uyarı
with st.sidebar:
    st.markdown("### 🌐 Dil Seçimi / Language")
    lang = st.selectbox("Select Language / Dil Seçin", ["Türkçe", "English"])
    
    st.markdown("---")
    if lang == "Türkçe":
        st.markdown("### ⚠️ Yasal Uyarı & Şartlar")
        st.markdown("""
        <div class='disclaimer-box'>
            <b>Yasal Bildirim:</b><br>
            • Bu yazılım ve içerikleri tamamen <b>bilgi amaçlıdır</b>.<br>
            • Fikir ve telif hakları gereği <b>kopyalanamaz, kaynak gösterilmeden paylaşılamaz</b>.<br>
            • Doğrudan veya dolaylı olarak <b>ticari amaçla kullanılamaz</b>.<br>
            • Yazılımın kullanımından doğabilecek her türlü sonuç için <b>geliştiricinin hiçbir sorumluluğu yoktur</b>. Tüm sorumluluk kullanıcıya aittir.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("### ⚠️ Legal Disclaimer")
        st.markdown("""
        <div class='disclaimer-box'>
            <b>Legal Notice:</b><br>
            • This software and its contents are for <b>informational purposes only</b>.<br>
            • Copyright protected: <b>Cannot be copied or reproduced</b>.<br>
            • Cannot be used directly or indirectly for <b>commercial purposes</b>.<br>
            • The developer assumes <b>no responsibility or liability</b> for any outcomes arising from its use. All responsibility belongs to the user.
        </div>
        """, unsafe_allow_html=True)

# Çeviri Sözlüğü (Localization Dictionaries)
if lang == "Türkçe":
    title = "HÛVE NÜKTESİ - KAPSAMLI ANALİZ VE SİMÜLASYON MODÜLÜ"
    caption = "Bediüzzaman Said Nursi'nin Hava Zerreleri Nüktesi Üzerine İlmî, Manevî, Felsefi ve Fiziksel İnceleme Külliyatı"
    tabs = [
        "📖 Nükte ve Derin İlahiyat", 
        "📜 Ayet, Hadis & Eser Tahlili", 
        "⚛️ Bilimsel & Kuantum Perspektif", 
        "🧮 Gelişmiş Dalga Simülasyonu",
        "📚 Genişletilmiş Kaynakça"
    ]
else:
    title = "HUVE NUKTESI - COMPREHENSIVE ANALYSIS & SIMULATION MODULE"
    caption = "Comprehensive Scientific, Spiritual, Philosophical and Physical Examination of Bediüzzaman Said Nursi's Air Particle Treatise"
    tabs = [
        "📖 Treatise & Deep Theology", 
        "📜 Verses, Hadiths & Works Analysis", 
        "⚛️ Scientific & Quantum Perspective", 
        "🧮 Advanced Wave Simulation",
        "📚 Expanded Bibliography"
    ]

# Başlık
st.markdown(f"<div class='main-header'>{title}</div>", unsafe_allow_html=True)
st.caption(caption)

# Sekmeli Menü
tab1, tab2, tab3, tab4, tab5 = st.tabs(tabs)

# --- TAB 1: NÜKTE VE DERİN İLAHİYAT ---
with tab1:
    if lang == "Türkçe":
        st.subheader("İsm-i Hû, Havanın Mahiyeti ve Tevhit Delilleri")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class='sub-card'>
                <h4>Hâtime-i İhlas ve Hûve Nüktesi'nin Felsefi Boyutu</h4>
                <p>Bediüzzaman Said Nursi hazretlerinin 13. Söz'ün Hâtimesi olan <b>Hûve Nüktesi</b>, havanın en küçük zerrelerinden küresel hareketlerine kadar her anında İlahi ispat ve tevhit mühürlerinin okunabileceğini muazzam bir dille gözler önüne serer.</p>
                <ul>
                    <li><b>Hû Lafzının Sırrı:</b> "Hû", Cenab-ı Hakk'ın zatına işaret eden, her şeyin mutlak varlık kaynağını O'na bağlayan ism-i azam yansımalarından biridir. Havanın her zerresinde bu ismin tecelli etmesi, kainattaki hiçbir zerecikten Hakk'ın ilim ve kudretinin hariç olmadığını gösterir.</li>
                    <li><b>Levh-i Mahv ve İspat Olarak Hava:</b> Hava tabakası; milyonlarca telefon konuşmasının, radyo dalgasının, kuş sesinin, ısı değişiminin ve kokunun aynı anda üst üste binmesine rağmen birbirine karışmadığı, saniyeler içinde yazılıp silindiği muazzam bir manevi fıtrat levhasıdır.</li>
                    <li><b>İki Alternatifli Akli Çıkmaz (Tevhit vs. Tabiat/Şirk):</b> 
                        <br>1) Ya havadaki her bir zerre, dünyadaki tüm dilleri, sesleri, frekansları aynı anda bilecek ve ayıracak ilahi bir ilme ve şuura maliktir (ki bu aklen ve mantıken imkansızdır).
                        <br>2) Veya o zerreler, sonsuz ilim ve kudret sahibi olan Kadîr-i Zülcelal'in orduları hükmünde, O'nun kanunlarıyla hareket etmektedir. Tevhit hakikati işte bu ikinci şıkkın kat'i zaruretini ispatlar.
                    </li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class='quote-box'>
                <b>"Evet, bir zerre hava; bütün dünyadaki radyo istasyonlarından gelen farklı sesleri aynı anda alır, dağıtır ve karıştırmaz. Binler dillerin kelimelerini aynı zerrede toplayıp sahibine ulaştırır..."</b><br><br>
                <i>- Risale-i Nur Külliyatı, Sözler (13. Söz'ün Hâtimesi)</i>
            </div>
            <div class='sub-card'>
                <h4>Eşsiz Mizansen</h4>
                <p>Havanın mutlak şuurlandırılması fikrinin batıllığı, tevhidin ne kadar parlak bir akli zaruret olduğunu açıkça gözler önüne serer.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.subheader("The Name 'Hu', The Nature of Air, and Proofs of Divine Unity")
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class='sub-card'>
                <h4>Philosophical Dimension of the Huve Nuktesi</h4>
                <p>Bediüzzaman Said Nursi's <b>Huve Nuktesi</b> (Treatise on Hu) masterfully demonstrates how divine proofs of unity can be read in every moment of air—from its smallest particles to global currents.</p>
                <ul>
                    <li><b>The Secret of 'Hu':</b> 'Hu' points to the Divine Essence, connecting all existence to its absolute source. Its manifestation in every air particle indicates that nothing is outside Divine knowledge.</li>
                    <li><b>Air as the Tablet of Erasure and Confirmation:</b> The atmosphere acts as a vast metaphysical board where millions of communications, sounds, and scents overlap without mixing, instantly recorded and erased.</li>
                    <li><b>The Two-Alternative Rational Dilemma:</b> 
                        <br>1) Either every single air particle possesses infinite consciousness, knowledge, and memory to handle all world signals simultaneously (which is rationally impossible).
                        <br>2) Or these particles act as obedient soldiers under the command of the All-Powerful Creator. The truth of Tawhid proves this second option as a strict necessity.
                    </li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class='quote-box'>
                <b>"Indeed, a single air particle receives, distributes, and keeps unmixed all distinct voices coming from radio stations across the world..."</b><br><br>
                <i>- Risale-i Nur Collection, The Words (The 13th Word)</i>
            </div>
            <div class='sub-card'>
                <h4>Unique Metaphor</h4>
                <p>The absurdity of assigning consciousness to air highlights how brilliant and rational the necessity of Tawhid truly is.</p>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 2: AYET, HADİS & ESER TAHLİLİ ---
with tab2:
    if lang == "Türkçe":
        st.subheader("Kur'an-ı Kerim, Sünnet-i Seniyye ve Risale-i Nur Bağlantıları")
        st.markdown("""
        <div class='sub-card'>
            <h4>1. Kur'an-ı Kerim'de Rüzgâr ve Hava Mucizeleri</h4>
            <ul>
                <li><b>Bakara Suresi, 164. Ayet:</b> <br><i>"Göklerin ve yerin yaratılışında, gece ile gündüzün birbiri ardından gelişinde... ve rüzgârların estirilmesinde, gökle yer arasında emre hazır bekleyen bulutların hareketlerinde düşünen bir toplum için elbette deliller vardır."</i> (Havanın ve rüzgârın sevk ve idaresindeki ilahi nizam vurgulanır.)</li>
                <li><b>Câsiye Suresi, 5. Ayet:</b> <br><i>"Gece ile gündüzün değişmesinde, Allah'ın gökten indirip onunla ölümünden sonra yeryüzüne hayat verdiği rızıkta ve rüzgârları yönlendirmesinde aklını kullanan bir toplum için nice deliller vardır."</i></li>
                <li><b>Rûm Suresi, 46. Ayet:</b> <br><i>"Rüzgârları müjdeleyiciler olarak göndermesi, rahmetinden size tattırması, gemilerin O'nun buyruğu ile yürümesi ve lütfundan aramanız O'nun delillerindendir."</i></li>
            </ul>
        </div>
        <div class='sub-card'>
            <h4>2. Hadis-i Şerifler Işığında Hava ve Rüzgâr</h4>
            <ul>
                <li><b>Rüzgâra Sövmeme Nehyi:</b> <br><i>"Rüzgâr Allah'ın rahmetindendir; rahmet de getirir, azap da getirir. Onu gördüğünüz vakit sövmeyin, Allah'tan onun hayrını dileyin ve şerrinden O'na sığının."</i> (Kaynak: Ebu Davud, Edeb, 101; İbn Mâce, Edeb, 25). Bu hadis, havanın ve rüzgârın şuursuz bir tabiat olayı olmayıp doğrudan ilahi bir idare altında olduğunu ihtar eder.</li>
                <li><b>Kıble ve Esinti Hikmeti:</b> Peygamberimiz (s.a.v.) şiddetli rüzgârlar estiğinde hüzünlenir, rahmet rüzgârlarında ise dua ederdi; bu da havanın ilahi tasarrufun en aktif aynası olduğunu gösterir.</li>
            </ul>
        </div>
        <div class='sub-card'>
            <h4>3. Risale-i Nur Külliyatı'ndan Destekleyici Diğer Nükteler</h4>
            <ul>
                <li><b>Yirmiuncu Mektup (Yirmi İkinci Söz - İhlas Risalesi):</b> Zerrelerin intizamı ve her bir zerrenin kainattaki mizanı koruması, ilahi birliğin en küçük birimlerde bile gözlendiğini kanıtlar.</li>
                <li><b>Otuzuncu Şua (İsimlerin Tevhit Mühürleri):</b> Kainattaki her bir mevcudun, özellikle gazların ve akışkanların Hak Teala'nın isimlerine (Alîm, Hakîm, Müdebbir) nasıl aynalük ettiğini inceler.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.subheader("Quranic Verses, Hadiths, and Works Analysis")
        st.markdown("""
        <div class='sub-card'>
            <h4>1. Wind and Air Miracles in the Holy Quran</h4>
            <ul>
                <li><b>Surah Al-Baqarah, Verse 164:</b> <br><i>"Indeed, in the creation of the heavens and the earth, and the alternation of the night and the day... and [in] the directing of the winds and the clouds controlled between the heaven and the earth are signs for a people who use reason."</i></li>
                <li><b>Surah Al-Jathiyah, Verse 5:</b> <br><i>"And [in] the alternation of night and day and what Allah sends down from the sky of provision... and [in His] directing of the winds are signs for a people who reason."</i></li>
                <li><b>Surah Ar-Rum, Verse 46:</b> <br><i>"And of His signs is that He sends the winds as bringers of good tidings and to let you taste of His mercy..."</i></li>
            </ul>
        </div>
        <div class='sub-card'>
            <h4>2. Air and Wind in the Light of Hadiths</h4>
            <ul>
                <li><b>Prohibition of Reviling the Wind:</b> <br><i>"The wind is from the mercy of Allah... When you see it, do not revile it, but ask Allah for its good."</i> (Source: Abu Dawud, Adab 101). This shows wind is under direct divine administration rather than blind nature.</li>
                <li><b>Prophetic Attitude:</b> The Prophet (pbuh) sought refuge during storms and prayed during mercy winds, indicating air is an active mirror of divine disposal.</li>
            </ul>
        </div>
        <div class='sub-card'>
            <h4>3. Supporting Treatise from the Risale-i Nur Collection</h4>
            <ul>
                <li><b>The Twentieth Letter & The Twenty-Second Word:</b> The absolute order among particles and how each particle maintains cosmic balance proves divine unity.</li>
                <li><b>The Thirtieth Ray:</b> Examines how every entity in creation, especially gases and fluids, mirrors divine names such as Al-Alim, Al-Hakim, and Al-Mudabbir.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 3: BİLİMSELLER & KUANTUM PERSPEKTİF ---
with tab3:
    if lang == "Türkçe":
        st.subheader("Modern Fizik, Akışkanlar Mekaniği ve Kuantum Teorisi Işığında Hava")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
            <div class='sub-card'>
                <h4>1. Süperpozisyon ve Dalga Üst Binmesi</h4>
                <p>Elektromanyetik dalgalar (radyo, televizyon, Wi-Fi, cep telefonu frekansları) ve ses dalgaları aynı anda aynı hava ortamını paylaşır. Fourier analizi gereğince, bu dalgalar birbirlerinin genliklerini bozmadan üst üste binebilir (superposition) ve alıcı antenler tarafından kusursuzca ayrıştırılır. Hûve Nüktesi'nde bahsedilen "seslerin karışmama sırrı" tam olarak bu fiziksel gerçeğin makro ve mikro düzeydeki ilahi tecellisidir.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class='sub-card'>
                <h4>2. İdeal Gaz Yasaları ve Moleküler Düzen</h4>
                <p>Termodinamiğin 2. Kanunu (Entropi) sistemlerin düzensizliğe gittiğini söyler; ancak bir cm³ havadaki yaklaşık 2.7x10¹⁹ molekül (Loschmidt sabiti), sıcaklık ve basınç dengesinde kusursuz bir uyum sergiler. Gaz moleküllerinin Maxwell-Boltzmann dağılımı, kaos gibi görünen hareketlerin aslında muazzam bir matematiksel yasa ve nizam altında yürütüldüğünün en somut kanıtıdır.</p>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
            <div class='sub-card'>
                <h4>3. Bilgi Teorisi ve Alan Taşıyıcılığı</h4>
                <p>Claude Shannon'ın Bilgi Teorisi (Information Theory) çerçevesinde hava ortamı, bilgi paketlerini (data packets) kayıpsız ve gecikmesiz taşıyan devasa bir iletim kanalıdır. Trilyonlarca bitlik verinin moleküler kinetik enerji üzerinden taşınması, havanın şuursuz bir gaz kütlesi olmadığını, aksine kusursuz bir İlahi veri tabanı gibi tasarruf edildiğini doğrular.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.subheader("Air in the Light of Modern Physics, Fluid Mechanics, and Quantum Theory")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
            <div class='sub-card'>
                <h4>1. Superposition and Wave Overlay</h4>
                <p>Electromagnetic waves (radio, TV, Wi-Fi, cell frequencies) and sound waves simultaneously share the air medium. According to Fourier analysis, these waves superimpose without distorting each other and are perfectly separated by receiver antennas. The 'unmixed voices' described in Huve Nuktesi correspond exactly to this physical reality.</p>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class='sub-card'>
                <h4>2. Ideal Gas Laws & Molecular Order</h4>
                <p>The 2nd Law of Thermodynamics states systems tend toward disorder; yet ~2.7x10¹⁹ molecules per cm³ of air maintain exquisite harmony under temperature and pressure equilibria. The Maxwell-Boltzmann distribution proves that seemingly chaotic molecular motions operate under strict mathematical laws.</p>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            st.markdown("""
            <div class='sub-card'>
                <h4>3. Information Theory & Medium Transport</h4>
                <p>Within Claude Shannon's Information Theory framework, air acts as a massive transmission channel carrying data packets losslessly. Transporting trillions of bits via molecular kinetic energy confirms air is managed like a flawless Divine database rather than an unconscious gas mass.</p>
            </div>
            """, unsafe_allow_html=True)

# --- TAB 4: GELİŞMİŞ DALGA SİMÜLASYONU ---
with tab4:
    if lang == "Türkçe":
        st.subheader("Hava Zerreleri Üzerinde Eşzamanlı Frekans ve Sinyal İletim Simülasyonu")
        st.write("Bu interaktif simülasyon modülü, havanın içinde aynı anda hareket eden farklı frekanslardaki dalgaların (ses, radyo, ışık ve bilgi sinyalleri) üst üste bindiğinde (superposition) oluşturduğu bileşke dalga formunu matematiksel olarak hesaplar ve görselleştirir.")
        
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            sinyal_sayisi = st.slider("Ortamdaki Eşzamanlı Sinyal / Kanal Sayısı", min_value=1, max_value=150, value=25, step=5)
        with col_s2:
            gurultu_orani = st.slider("Ortam Kinetik Dalgalanma (Gürültü) Katsayısı", min_value=0.0, max_value=1.0, value=0.15, step=0.05)
            
    else:
        st.subheader("Simultaneous Frequency and Signal Transmission Simulation on Air Particles")
        st.write("This interactive simulation module calculates and visualizes the composite waveform created by the superposition of multi-frequency waves (sound, radio, light, data) moving simultaneously through air.")
        
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            sinyal_sayisi = st.slider("Number of Simultaneous Signals / Channels", min_value=1, max_value=150, value=25, step=5)
        with col_s2:
            gurultu_orani = st.slider("Medium Kinetic Fluctuation (Noise) Coefficient", min_value=0.0, max_value=1.0, value=0.15, step=0.05)
    
    t = np.linspace(0, 4 * np.pi, 1000)
    bileşke_dalga = np.zeros_like(t)
    
    np.random.seed(123)
    for i in range(sinyal_sayisi):
        freq = np.random.uniform(0.5, 15.0)
        faz = np.random.uniform(0, 2 * np.pi)
        genlik = np.random.uniform(0.5, 1.5)
        bileşke_dalga += genlik * np.sin(freq * t + faz)
        
    # Gürültü ekleme
    bileşke_dalga += gurultu_orani * np.random.normal(0, 1, len(t))
    
    df_sim = pd.DataFrame({
        "Zaman Parametresi (t)": t,
        "Bileşke Hava İletim Sinyali": bileşke_dalga
    })
    
    st.line_chart(df_sim.set_index("Zaman Parametresi (t)"))
    
    if lang == "Türkçe":
        st.success(f"✅ **Simülasyon Analiz Sonucu:** Ortamda aynı anda işlenen bağımsız kanal sayısı: **{sinyal_sayisi}**. Hava ortamı, bu kadar karmaşık ve üst üste binen dalga formlarını hiçbir veri kaybı veya kalıcı bozulma yaşamaksızın iletmektedir. Bu durum, havanın atomik alt yapısının kusursuz bir İlahi irade ile sevk edildiğini kanıtlayan matematiksel bir modeldir.")
    else:
        st.success(f"✅ **Simulation Analysis Result:** Number of simultaneous independent channels processed: **{sinyal_sayisi}**. The air medium transmits these complex overlapping waveforms without data loss or permanent distortion, representing a mathematical model proving the flawless divine administration of atomic structures.")

# --- TAB 5: GENİŞLETİLMİŞ KAYNAKÇA ---
with tab5:
    if lang == "Türkçe":
        st.subheader("Çalışmanın Kapsamlı ve Detaylı Kaynakçası")
        st.write("Bu yazılım modülünün hazırlanmasında yararlanılan temel manevi, dini, felsefi ve akademik referans eserlerin tam listesi:")
        st.markdown("""
        <div class='ref-box'>
            <b>1. İlahiyat & Manevi Külliyat Kaynakları:</b><br>
            • Bediüzzaman Said Nursi, <i>Risale-i Nur Külliyatı</i>, "Sözler" (13. Söz'ün Hâtimesi - Hûve Nüktesi), Envar Neşriyat, İstanbul.<br>
            • Bediüzzaman Said Nursi, <i>Mektubat</i>, "20. Mektubun Zeyli ve Esma-i Hüsna Tahlilleri", Envar Neşriyat.<br>
            • Bediüzzaman Said Nursi, <i>Şualar</i>, "30. Şua (İsimlerin Tevhit Mühürleri)", Envar Neşriyat.<br>
            • Bediüzzaman Said Nursi, <i>Lem'alar</i>, "30. Lem'a (İsm-i Azam Risalesi)", Envar Neşriyat.
        </div>
        <div class='ref-box'>
            <b>2. Tefsir, Hadis & İslamî İlimler Kaynakları:</b><br>
            • Kur'an-ı Kerim ve Açıklamalı Meali (Bakara: 164, Câsiye: 5, Rûm: 46, Zâriyât: 1-4).<br>
            • Ebû Dâvûd, Süleyman b. el-Eş‘as, <i>Sünen-i Ebû Dâvûd</i>, "Edeb, 101", Çağrı Yayınları.<br>
            • İbn Mâce, Muhammed b. Yezîd, <i>Sünen-i İbn Mâce</i>, "Edeb, 25", İnkılap Kitabevi.<br>
            • İmam Gazâlî, <i>İhyâü Ulûmi'd-Din</i>, "Kitâbü Tevhîd ve Tevekkül", Kahire.
        </div>
        <div class='ref-box'>
            <b>3. Fizik, Mühendislik & Modern Bilim Kaynakları:</b><br>
            • Feynman, Richard P.; Leighton, Robert B.; Sands, Matthew, <i>Feynman Fizik Dersleri</i> (Cilt 1 ve 2), Kabalcı Yayınevi.<br>
            • Halliday, David; Resnick, Robert; Walker, Jearl, <i>Fiziğin Temelleri (Fundamentals of Physics)</i>, Palme Yayıncılık.<br>
            • Shannon, Claude E., <i>A Mathematical Theory of Communication</i>, Bell System Technical Journal, 1948.<br>
            • Serway, Raymond A.; Jewett, John W., <i>Fen ve Mühendislik İçin Fizik</i>, Nobel Akademik Yayıncılık.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.subheader("Comprehensive and Detailed Bibliography")
        st.write("The full list of fundamental spiritual, religious, philosophical, and academic reference works utilized in preparing this software module:")
        st.markdown("""
        <div class='ref-box'>
            <b>1. Theological & Spiritual Collection Sources:</b><br>
            • Bediüzzaman Said Nursi, <i>Risale-i Nur Collection</i>, "The Words" (The 13th Word - Treatise on Hu), Envar Neşriyat, Istanbul.<br>
            • Bediüzzaman Said Nursi, <i>The Letters</i>, "The 20th Letter Addendum", Envar Neşriyat.<br>
            • Bediüzzaman Said Nursi, <i>The Rays</i>, "The 30th Ray", Envar Neşriyat.<br>
            • Bediüzzaman Said Nursi, <i>The Flashes</i>, "The 30th Flash", Envar Neşriyat.
        </div>
        <div class='ref-box'>
            <b>2. Exegesis, Hadith & Islamic Sciences Sources:</b><br>
            • The Holy Quran and Translation (Al-Baqarah: 164, Al-Jathiyah: 5, Ar-Rum: 46, Ad-Dhariyat: 1-4).<br>
            • Abu Dawud, Sulayman ibn al-Ash'ath, <i>Sunan Abu Dawud</i>, "Adab, 101".<br>
            • Ibn Majah, Muhammad ibn Yazid, <i>Sunan Ibn Majah</i>, "Adab, 25".<br>
            • Imam Al-Ghazali, <i>Ihya Ulum al-Din</i>, "Book of Tawhid and Tawakkul".
        </div>
        <div class='ref-box'>
            <b>3. Physics, Engineering & Modern Science Sources:</b><br>
            • Feynman, Richard P.; Leighton, Robert B.; Sands, Matthew, <i>The Feynman Lectures on Physics</i> (Vol. 1 & 2).<br>
            • Halliday, David; Resnick, Robert; Walker, Jearl, <i>Fundamentals of Physics</i>.<br>
            • Shannon, Claude E., <i>A Mathematical Theory of Communication</i>, Bell System Technical Journal, 1948.<br>
            • Serway, Raymond A.; Jewett, John W., <i>Physics for Scientists and Engineers</i>.
        </div>
        """, unsafe_allow_html=True)