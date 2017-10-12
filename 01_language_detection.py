import langdetect

print langdetect.detect_langs('port color')
# [es:0.714281606856, it:0.142859348168, fr:0.142856928761]

print langdetect.detect_langs('The sky above the port was the color of television, tuned to a dead channel.')
# [en:0.999997611175]
