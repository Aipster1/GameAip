/* flipSevenCards.js*/

/* Wird augerufen wenn die DOM (Document Object Model) geladen ist damit alle Elemente die benötigt werden geladen wurden (da diese hier wohl bearbeitet werden)*/
document.addEventListener("DOMContentLoaded", () => {
  // applyFan(hand) — berechnet Position/Rotation/zIndex für alle Karten in einer Hand
  function applyFan(hand) {
    // Alle .card Elemente in der übergebenen Hand als Array
    const cards = Array.from(hand.querySelectorAll('.card'));
    const n = cards.length;
    if (n === 0) return; // keine Karten -> nichts zu tun

    // -------------------------------
    // Sauberer Neuaufbau der Event-Handler:
    // Wenn applyFan mehrfach aufgerufen wird (z.B. nach Resize),
    // löschen wir bestehende on*-Handler bevor wir neue setzen.
    // (Wir verwenden das on*-Pattern statt addEventListener, damit
    //  wir durch Zuweisung gezielt überschreiben können.)
    // -------------------------------
    cards.forEach(c => {
      c.onmouseenter = null;
      c.onmouseleave = null;
      c.onclick = null;
    });

    // -------------------------------
    // Parameter aus data-attributes (können pro Hand verschieden sein)
    // -------------------------------
    const spread = parseFloat(hand.dataset.spread) || 60;   // Gesamtwinkel in Grad
    let spacing = parseFloat(hand.dataset.spacing) || 38;  // horizontaler Abstand in px
    const radius = parseFloat(hand.dataset.radius) || 22;  // wie stark die Karte "hochgezogen" wird (px)
    const orientation = (hand.dataset.orientation || "bottom").toLowerCase();

    // Auto-Spacing: verhindert bei vielen Karten zu große Lücken
    const containerW = hand.clientWidth || (window.innerWidth * 0.6);
    const maxSpacing = containerW / Math.max(6, n);
    spacing = Math.min(spacing, maxSpacing);

    // Schrittwinkel zwischen Nachbarkarten (gleichmäßig verteilt)
    const step = n > 1 ? spread / (n - 1) : 0;

    // Basisrotation abhängig von Orientierung (z.B. top = 180°)
    const orientRot = { bottom: 0, top: 180, left: -90, right: 90 }[orientation] || 0;

    // Transform-Origin-Werte pro Orientierung (wichtig für optische Ergebnisse)
    const origins = {
      top: "50% 0%",
      bottom: "50% 100%",
      left: "0% 50%",
      right: "100% 50%"
    };
    const transformOrigin = origins[orientation] || "50% 100%";

    // -------------------------------
    // Für jede Karte berechnen wir:
    // - rel: zentrierte Indexposition (z.B. -2,-1,0,1,2)
    // - angle: Rotation in Grad
    // - translateX: horizontale Lage relativ zur Mitte
    // - translateY: leichte Anhebung der Außenkarten
    // - z: zIndex zur Stapelreihenfolge
    // Wir speichern Basiswerte in data-Attributen zum späteren Zurücksetzen.
    // -------------------------------
    cards.forEach((card, i) => {
      const rel = i - (n - 1) / 2; // zentrierte Position
      const angle = rel * step + orientRot;
      const translateX = rel * spacing;
      const translateY = 0//-Math.abs(rel) * radius;
      const z = 100 + i; // Basis-zIndex (100+ i sorgt für konsistente Reihenfolge)

      // Setze transform-origin passend zur Orientierung
      card.style.transformOrigin = transformOrigin;

      // Setze Basis-zIndex (wird später beim Mouseleave wiederhergestellt)
      card.style.zIndex = z;

      // Erzeuge die Basis-Transform-String (rotate + translate)
      const baseTransform = `translateX(${translateX}px) translateY(${translateY}px) rotate(${angle}deg)`;

      // Wende Basis-Transform an (das ist der "normalzustand" der Karte)
      card.style.transform = baseTransform;

      // Speichere Basisdaten im DOM (dataset) für späteres Zurücksetzen
      card.dataset.baseTransform = baseTransform;
      card.dataset.origZ = z;
      card.dataset.index = i; // optional: index speichern, kann für Debug hilfreich sein

      // -------------------------------
      // Click-Handler: extrahiert Dateiname aus src und loggt ihn.
      // Das kann beim Debuggen helfen (welche Karte wurde geklickt).
      // -------------------------------
      card.onclick = () => {
        const fullSrc = card.getAttribute('src') || "";
        const fileName = fullSrc.split('/').pop();
        console.log('Karte geklickt:', fileName);
      };

      // -------------------------------
      // Hover-Verhalten (mouseenter / mouseleave)
      // - onmouseenter: Karte nach vorne bringen (hoher zIndex) und
      //                 die Basistransformation erweitern (anheben + leicht skalieren)
      // - onmouseleave: transform und zIndex auf die gespeicherten Basiswerte zurücksetzen
      //
      // Wichtig: wir ergänzen das baseTransform (nicht ersetzen), so bleibt die Rotation erhalten.
      // -------------------------------
      card.onmouseenter = () => {
        // Ganz nach vorne bringen (großer Wert, damit andere UI-Elemente nicht betroffen sind)
        card.style.zIndex = 10000;

        // Kombiniere Basis-Transform mit zusätzlicher visueller Hervorhebung
        // (translateY(-18px) hebt die Karte, scale(1.04) macht sie leicht größer)
        card.style.transform = card.dataset.baseTransform + ' translateY(-18px) scale(1.04)';
      };
      card.onmouseleave = () => {
        // zIndex und transform auf Originalwerte zurücksetzen
        card.style.zIndex = card.dataset.origZ;
        card.style.transform = card.dataset.baseTransform;
      };
    });
  } // Ende applyFan

  // -------------------------------
  // Initialausführung: wende applyFan auf alle .hand Elemente an
  // -------------------------------
  document.querySelectorAll('.hand').forEach(hand => applyFan(hand));

  // -------------------------------
  // Responsive: bei Resize neu berechnen (debounced)
  // Damit werden z.B. spacing/Positionen an neue Breite angepasst.
  // -------------------------------
  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
      document.querySelectorAll('.hand').forEach(hand => applyFan(hand));
    }, 120); // 120ms debounce
  });

  // -------------------------------
  // Toggle-Button: Umschalten zwischen "Fächer" und "Gerade" Ansicht
  // - .hand.straight Klasse steuert das CSS für die gerade Ansicht
  // - Beim Zurückwechsel in Fächeransicht rufen wir applyFan erneut auf,
  //   damit Basis-Transform- und dataset-Werte wieder korrekt gesetzt werden.
  // -------------------------------
  const toggleBtn = document.querySelector(".toggle-view-btn");
  const hand = document.querySelector(".hand"); // einfache Annahme: erste Hand
  let isStraight = false;
  if (toggleBtn && hand) {
    toggleBtn.addEventListener("click", () => {
      isStraight = !isStraight;
      hand.classList.toggle("straight", isStraight);

      // Buttontext anpassen (deutsch)
      toggleBtn.textContent = isStraight ? "Gerade Ansicht" : "Fächeransicht";

      // Wenn wir wieder in die Fächeransicht wechseln, neu anordnen
      if (!isStraight) {
        applyFan(hand);
      }
    });
  }
}); // Ende DOMContentLoaded
