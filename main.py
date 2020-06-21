from summariser import Summariser

paragraph = """Before time began, there was the Cube. We know not where it comes from,
            only that it holds the power to create worlds and fill them with life. 
            That was how our race was born. For a time, we lived in harmony, but like all great power, 
            some wanted it for good, others for evil. And so began the war - 
            a war that ravaged our planet until it was consumed by death, 
            and the Cube was lost to the far reaches of space. 
            We scattered across the galaxy, hoping to find it and rebuild our home, searching every star, every world.
            And just when all hope seemed lost, message of a new discovery drew us to an unknown planet called... Earth. 
            But we were already too late.
            
            With the All Spark gone, we cannot return life to our planet. 
            And fate has yielded its reward: a new world to call... home. 
            We live among its people now, hiding in plain sight... but watching over them in secret... waiting... protecting.
            I have witnessed their capacity for courage, and though we are worlds apart, like us, 
            there's more to them than meets the eye. I am Optimus Prime, 
            and I send this message to any surviving Autobots taking refuge among the stars: We are here... we are waiting.
            
            Earth. Birthplace of the human race, a species much like our own. 
            Capable of great compassion... and great violence. For in our quest to protect the humans, 
            a deeper revelation dawns; our worlds have met before. 
            For the last two years, an advanced team of new Autobots has taken refuge here under my command. 
            Together, we form an alliance with the humans, a secret but brave squad of soldiers. 
            A classified strike team called NEST. We hunt for what remains of our Decepticon foes, 
            hiding in different countries around the globe.
            
            Our races united by a history long forgotten, and a future we shall face together. 
            I, am Optimus Prime, and I send this message so that our pasts will always be remembered. 
            For in those memories, we live on."""

freq_table = Summariser.create_frequency_table(paragraph)

print(freq_table)

sentence = Summariser.sentence_tokenize(paragraph)

sentence_scores = Summariser.score_sentences(sentence, freq_table)

print(sentence_scores)

threshold = Summariser.find_average_score(sentence_scores)

print(threshold)

summary = Summariser.generate_summary(sentence, sentence_scores, 0.75 * threshold)

print(summary)