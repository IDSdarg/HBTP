import hbtp
import use_preprocess as up
up.use_preprocess()

from format_event import *
from format_story import *
from split_train_test import *


def get_formatted():
    formatted_stories = get_formatted_stories()
    formatted_events = get_formatted_events(story_to_id=formatted_stories.story_to_id)
    return formatted_events, formatted_stories


def get_corpus(corpus_cls, f_events: FormattedEvent, f_stories: FormattedStory):
    try:
        return corpus_cls(
            vocab=[f_stories.id_to_word[i] for i in range(len(f_stories.id_to_word))],
            word_ids=f_stories.word_ids,
            word_cnt=f_stories.word_cnt,
            child_to_parent_and_story=f_events.child_to_parent_and_story,
            story_to_users=f_events.story_to_users,
            n_topic=100,
        )
    except:
        return corpus_cls(
            vocab=[f_stories.id_to_word[i] for i in range(len(f_stories.id_to_word))],
            word_ids=f_stories.word_ids,
            word_cnt=f_stories.word_cnt,
            n_topic=100,
        )


def run_model(model_cls, corpus, n_topic=100):
    _model = model_cls(
        n_topic=n_topic,
        n_voca=corpus.n_voca,
    )
    _model.fit(corpus)
    return _model


if __name__ == '__main__':
    events, stories = get_formatted()
    run_model(hbtp.HBTP, get_corpus(hbtp.Corpus, events, stories))
