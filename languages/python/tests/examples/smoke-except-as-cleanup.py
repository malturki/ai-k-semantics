#tryExceptCases({
raise #exception(ValueError);
}, #exceptAs(ValueError, err, {
seen = (err == err);
}));
seen;
